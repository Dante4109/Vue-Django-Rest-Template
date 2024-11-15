import pytest
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestAuthJWTAPIViews(TestCase):
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
        # create user account for test
        User.objects.create_user(
            email=self.user_basic_data["email"],
            password=self.user_basic_data["password"],
        )

        # create admin account for test
        User.objects.create_user(
            email=self.user_admin_data["email"],
            password=self.user_admin_data["password"],
        )

    def test_get_access_token_basic_user(self):
        """Obtains an access token and a refresh token
        using the basic user account instance.
        """
        url = reverse("token_obtain_pair")

        # call the url
        response = self.client.post(url, data=self.user_basic_data)

        # assertions
        # - json
        # - status

        print(response)

        assert response.json() != None
        assert response.json()["refresh"]
        assert response.json()["access"]
        assert response.status_code == 200

    def test_get_access_token_admin_user(self):
        """Obtains an access token and a refresh token
        using the admin user account instance.
        """
        url = reverse("token_obtain_pair")

        # call the url
        response = self.client.post(url, data=self.user_basic_data)

        # assertions
        # - json
        # - status
        assert response.json() != None
        assert response.json()["refresh"]
        assert response.json()["access"]
        assert response.status_code == 200
