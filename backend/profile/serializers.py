from rest_framework import serializers
from .models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "uuid",
            "username",
            "last_updated",
            "first_name",
            "last_name",
            "age",
            "records",
            "pronouns",
            "region",
            "facts",
            "ImgUrl",
            "extra_data",
            "image_collection",
            "user_settings",
        )
