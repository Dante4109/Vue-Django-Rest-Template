from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserEmailVerification

UserModel = get_user_model()


class UserEmailVerificationSerializer(serializers.Serializer):

    class Meta:
        model = UserEmailVerification
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data["email"],
            name=validated_data["name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        if "email" in validated_data:
            instance.email = validated_data.pop("email")

        if "profile" in validated_data:
            instance.profile = validated_data.pop("profile")

        if "name" in validated_data:
            instance.name = validated_data.pop("name")

        if "is_verified" in validated_data:
            instance.is_verified = validated_data.pop("is_verified")

        instance.save()
        return instance

    class Meta:
        model = UserModel
        depth = 3
        fields = (
            "id",
            "email",
            "password",
            "profile",
            "profile_id",
            "name",
            "last_login",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "last_updated",
            "is_verified",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }


class CustomTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
