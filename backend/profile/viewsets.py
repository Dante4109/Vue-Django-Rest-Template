from django.http import Http404
from requests import Response
from backend.profile.models import UserProfile
from backend.profile.serializers import ProfileSerializer
from rest_framework.permissions import (
    BasePermission,
    AllowAny,
    SAFE_METHODS,
    IsAuthenticated,
    IsAdminUser,
)
from backend.users.viewsets import IsSuperUser, IsUser
from rest_framework import status, viewsets, views


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    # def create(self, request):
    #     post_data = request.data
    #     serializer = ProfileSerializer(data=post_data)
    #     if serializer.is_valid():
    #         serializer.save(owner=self.request.user)
    #         return Response(serializer.data, status=201)
    #     print(request.data)
    #     return Response({"error": "Data is invalid."}, status=400)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"UserProfile deleted"}, status=200)
        except Http404:
            return Response({"UserProfile not found"}, status=404)

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = IsAuthenticated
        if self.action == "DELETE":
            self.permission_classes = [
                IsAdminUser,
            ]
        return super(ProfileViewSet, self).get_permissions()
