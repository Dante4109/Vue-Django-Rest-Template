import os, django

django.setup()
from django.contrib.auth import get_user_model
from hypothesis.extra.django import TestCase
import pytest
from hypothesis import strategies as st, given
from backend.profile.models import UserProfile
from rest_framework.test import APIClient

from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestUserProfile(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_basic_data = {
            "email": "basic_user@example.com",
            "password": "password",
        }
        self.user_admin_data = {
            "email": "admin_user@example.com",
            "password": "password",
        }

        # create user account for test
        User = get_user_model()
        User.objects.create_user(
            email=self.user_basic_data["email"],
            password=self.user_basic_data["password"],
        )

        # create admin account for test
        User.objects.create_user(
            email=self.user_admin_data["email"],
            password=self.user_admin_data["password"],
        )

    def test_profile_can_be_created(self):
        """
        Tests if a UserProfile can be created.
        This will not write to the DB.
        """

        profile1 = mixer.blend(UserProfile, first_name="Tom")

        profile1 = UserProfile.objects.last()  # getting the last student

        assert profile1.first_name == "Tom"
