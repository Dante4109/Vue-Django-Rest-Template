import pytest
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from backend.profile.models import UserProfile

from mixer.backend.django import mixer

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestUserProfileAPIViews(TestCase):
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

        User = get_user_model()
        # create basic user account for test
        User.objects.create_user(
            email=self.user_basic_data["email"],
            password=self.user_basic_data["password"],
        )

        # create super user account for test
        User.objects.create_superuser(
            email=self.user_admin_data["email"],
            password=self.user_admin_data["password"],
        )

        # get auth token
        url = reverse("token_obtain_pair")

        # call the url
        response = self.client.post(url, data=self.user_admin_data)
        self.admin_access_token = response.json()["access"]

        response = self.client.post(url, data=self.user_basic_data)
        self.basic_access_token = response.json()["access"]

    def test_public_profile_list(self):
        # create temp profiles

        profile1 = mixer.blend(UserProfile, first_name="John", last_name="Buck")
        profile2 = mixer.blend(UserProfile, first_name="Mary", last_name="Doe")

        url = reverse("profilelist_public")

        # call the url
        response = self.client.get(url)

        # print(dir(response), "response")

        # aseertions
        # - json
        # - status

        assert response.json() != None
        assert response.json()[0]["first_name"] == "John"
        assert response.json()[0]["last_name"] == "Buck"
        assert response.json()[1]["first_name"] == "Mary"
        assert response.json()[1]["last_name"] == "Doe"
        assert UserProfile.objects.count() == 2
        assert len(response.json()) == 2
        assert response.status_code == 200

    def test_create_profile_api_admin(self):
        # headers
        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(self.admin_access_token)}

        # data
        input_data = {"first_name": "John", "last_name": "Buck"}

        url = "/api/UserProfile/"

        # call the url
        response = self.client.post(
            url,
            data=input_data,
            **header,
        )

        # assertions
        assert response.status_code == 201
        assert response.json() != None
        assert response.json()["first_name"] == "John"
        assert response.json()["last_name"] == "Buck"
        assert UserProfile.objects.count() == 1
        assert url == "/api/UserProfile/"

    def test_create_profile_api_basic(self):
        # headers
        header = {"HTTP_AUTHORIZATION": "Bearer {}".format(self.admin_access_token)}

        # data
        input_data = {"first_name": "John", "last_name": "Buck"}

        url = "/api/UserProfile/"

        # call the url
        response = self.client.post(
            url,
            data=input_data,
            **header,
        )

        # assertions
        assert response.status_code == 201
        assert response.json() != None
        assert response.json()["first_name"] == "John"
        assert response.json()["last_name"] == "Buck"
        assert UserProfile.objects.count() == 1
        assert url == "/api/UserProfile/"
