from backend.profile import views
from rest_framework.permissions import BasePermission, AllowAny, SAFE_METHODS
from backend.users import models
from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets, views

from .models import UserProfile
from .serializers import ProfileSerializer
from django.http import Http404, JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
import json
import requests


# TO-DO Replace error handling print statements with log statements.


class ProfilePublicListView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = UserProfile.objects.all()
        serializer_class = ProfileSerializer(queryset, many=True)
        return Response(serializer_class.data)


class ProfilePublicView(views.APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        return UserProfile.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        try:
            queryset = UserProfile.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({"UserProfile not found"}, status=404)

        serializer_class = ProfileSerializer(queryset, data=request.data)
        if serializer_class.is_valid():
            return JsonResponse(serializer_class.data, status=200)
        else:
            return JsonResponse({"Invalid data entered"}, status=404)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileSetup(views.APIView):
    def post(self, request, *args, **kwargs):

        user_json = request.data.get("user", None)
        if not user_json:
            print("No user was provided when attempting to create UserProfile.")
            return JsonResponse({"error": "No user provided."}, status=401)

        try:
            user = get_user_model().objects.get(id=user_json["id"])
        except ObjectDoesNotExist:
            print("Unable to create new UserProfile. User does not exist")
            return JsonResponse({"error": "User does not exist."}, status=404)

        profile_defaults = {
            "last_updated": None,
            "first_name": "",
            "last_name": "",
            "age": None,
            "records": "",
            "pronouns": "",
            "region": "",
            "facts": "",
            "ImgUrl": "none",
        }

        NewProfile, created = UserProfile.objects.get_or_create(
            id=user.profile_id, defaults=profile_defaults
        )
        NewProfile.save()
        user.profile = NewProfile
        user.save()

        serialized = serializers.serialize(
            "json",
            [
                NewProfile,
            ],
            fields=(
                "id",
                "username",
                "last_updated",
                "first_name",
                "last_name",
                "age",
                "records",
                "games",
                "pronouns",
                "region",
                "facts",
                "ImgUrl",
            ),
        )

        serialized = json.loads(serialized)
        instance = serialized[0]["fields"]

        # add pk to instance
        instance["id"] = serialized[0]["pk"]

        return JsonResponse(instance, safe=False, status=201)
