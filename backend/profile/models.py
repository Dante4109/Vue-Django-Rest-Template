from django.db import models
from django.db.models import JSONField
from django.dispatch import receiver
import uuid


class UserProfile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    username = models.CharField(default="none", max_length=65)
    last_updated = models.DateTimeField(auto_now=True)
    first_name = models.CharField(default="none", max_length=20)
    last_name = models.CharField(max_length=20, default="none")
    age = models.DateField(null=True)
    pronouns = JSONField(default=dict)
    records = JSONField(default=dict)
    facts = JSONField(default=dict)
    region = models.CharField(max_length=50, default="none")
    ImgUrl = models.CharField(default="none", max_length=255)
    extra_data = JSONField(default=dict)
    user_settings = JSONField(default=dict)
    image_collection = JSONField(default=dict)

    def __str__(self):
        return self.username
