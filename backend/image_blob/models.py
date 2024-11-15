from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from backend.profile.models import UserProfile
import uuid


def get_upload_path(instance, filename):
    return "UserProfile/{0}/Images/{1}".format(instance.profile.uuid, filename)


class ImageBlob(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    img_url = models.ImageField(upload_to=get_upload_path)
    description = models.TextField(max_length=255, default="none")
    name = models.CharField(max_length=100, default="Unknown image")
    date_created = models.DateTimeField(default=timezone.now)
    size = models.CharField(max_length=100, default="Unknown size")
    filetype = models.CharField(max_length=100, default="Unknown file type")
    profile = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.SET_NULL
    )

    def _str_(self):
        return self.image.name
