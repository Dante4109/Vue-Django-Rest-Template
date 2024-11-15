from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from backend import profile
from backend.users.serializers import UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .permissions import IsOwner
from django.http import Http404
from backend.profile.views import ProfileSetup
import json


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                print(obj == request.user)
                return obj == request.user
        else:
            return False


class UserViewSet(viewsets.ViewSet):
    permission_classes = [
        IsUser,
    ]

    def list(self, request):
        queryset = get_user_model().objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        post_data = request.data
        serializer = UserSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=201)
        print(request.data)
        return Response({"error": "Data is invalid."}, status=400)

    def update(self, request, pk=None):
        post_data = request.data
        obj = get_user_model().objects.get(pk=pk)
        self.check_object_permissions(self.request, obj)
        serializer = UserSerializer(instance=obj, data=post_data, partial=True)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=204)
        print(request.data)
        return Response({"error": "Data is invalid."}, status=400)

    def partial_update(self, request, pk=None):
        patch_data = request.data
        obj = get_user_model().objects.get(pk=pk)
        self.check_object_permissions(self.request, obj)
        serializer = UserSerializer(instance=obj, data=patch_data, partial=True)
        if "email" in patch_data.keys():
            email_exists = True
            try:
                get_user_model().objects.get(email=patch_data["email"])
            except:
                email_exists = False
            else:
                if email_exists:
                    return Response({"error": "Email is already in use."}, status=409)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            # serializer.save()
            return Response(serializer.data, status=204)
        print(request.data)
        return Response({"error": "Data is invalid."}, status=400)

    def retrieve(self, request, pk=None):
        queryset = get_user_model().objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(self.request, obj)
        serializer = UserSerializer(obj)
        return Response(serializer.data)

    def delete(self, request):
        if "email" in request.data.keys():
            user_email = request.data["email"]
            try:
                obj = get_user_model().objects.get(email=user_email)
            except:
                return Response(
                    (f"error: User: {user_email} was not found"), status=404
                )
            self.check_object_permissions(self.request, obj)
            try:
                obj.delete()
                return Response((f"User: {user_email} was deleted"), status=204)
            except:
                return Response((f"User: {user_email} was not deleted"), status=500)
        else:
            return Response(
                {"error": "Data is invalid. Please provide a valid email."}, status=400
            )

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = (AllowAny,)
        if self.action == "list":
            self.permission_classes = [IsSuperUser]
        if self.action == "detail":
            self.permission_classes = (
                [
                    IsUser,
                ],
            )
        if self.action == "DELETE":
            self.permission_classes = [
                IsSuperUser,
            ]
        return super(UserViewSet, self).get_permissions()
