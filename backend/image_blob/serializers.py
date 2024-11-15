from rest_framework import serializers
from .models import ImageBlob
from backend.profile.models import UserProfile
from backend.profile.serializers import ProfileSerializer

size = serializers.SerializerMethodField()
name = serializers.SerializerMethodField()
filetype = serializers.SerializerMethodField()
date_created = serializers.SerializerMethodField()


class ImageBlobSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    profile_id = serializers.IntegerField(write_only=True, allow_null=True)

    class Meta:
        model = ImageBlob
        fields = (
            "id",
            "uuid",
            "img_url",
            "date_created",
            "size",
            "name",
            "filetype",
            "description",
            "profile",
            "profile_id",
        )

    def get_size(self, obj):
        file_size = ""
        if obj.image and hasattr(obj.image, "size"):
            file_size = obj.image.size
        return file_size

    def get_name(self, obj):
        file_name = ""
        if obj.image and hasattr(obj.image, "name"):
            file_name = obj.image.name
        return file_name

    def get_filetype(self, obj):
        filename = obj.image.name
        return filename.split(".")[-1]

    def get_date_created(self, obj):
        date_added = obj.date_created
        return date_added
