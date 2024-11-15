import os
import pytest

import os, django

django.setup()

from django.test import TestCase
from backend.users.models import CustomUser, UserManager

umanager = UserManager()


class TestUserModel(TestCase):
    def test_user_can_be_created(self):

        user1 = UserManager.create_user(
            self,
            email="Jdoe@example.com",
            password="Password",
            name="John Doe",
        )

        self.assertEqual(user1.name == "John Doe")
