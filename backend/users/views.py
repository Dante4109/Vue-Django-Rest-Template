import os

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import viewsets, permissions

from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from django_rest_passwordreset.views import get_password_reset_token_expiry_time
from django_rest_passwordreset.models import ResetPasswordToken
from .serializers import *
from rest_framework.response import Response
from rest_framework import parsers, renderers, status
from rest_framework.views import APIView
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.shortcuts import render

# Create your views here.
from .models import UserEmailVerification, CustomUser

# from vuedj.constants import site_url, site_full_name, site_shortcut_name


class UserEmailVerificationView(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    queryset = UserEmailVerification.objects.all()
    serializer_class = UserEmailVerificationSerializer

    def post(self, request):
        post_data = request.data
        email_verification = get_object_or_404(
            UserEmailVerification, verification_token=post_data["token"]
        )
        try:
            user = get_object_or_404(CustomUser, id=email_verification.user_id)
            user.is_verified = True
            user.save()
            email_verification.delete()
            return Response({"Email Successfully Verified"}, status=200)
        except Http404:
            return Response({"Token Not Found"}, status=404)

        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomPasswordResetView:
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
        """
        Handles password reset tokens
        When a token is created, an e-mail needs to be sent to the user
        """

        # locally defining static values for testing purposes
        # site_url = "https://www.affinitycore.com"
        site_url = os.getenv("SITE_URL")
        site_full_name = os.getenv("SITE_FULL_NAME")
        site_shortcut_name = os.getenv("SITE_SHORTCUT_NAME")
        smtp_url = os.getenv("SMTP_URL")
        # Testing URL Full Path

        # send an e-mail to the user
        context = {
            "current_user": reset_password_token.user,
            "username": reset_password_token.user.username,
            "email": reset_password_token.user.email,
            "reset_password_url": "{}/password_reset/{}".format(
                site_url, reset_password_token.key
            ),
            "site_name": site_shortcut_name,
            "site_domain": smtp_url,
        }

        # render email text

        email_html_message = render_to_string("user_reset_password.html", context)
        email_plaintext_message = render_to_string("user_reset_password.txt", context)

        # email_html_message = "test html message\n\n" + context['reset_password_url']
        # email_plaintext_message = "test text message\n\n" + context['reset_password_url']

        msg = EmailMultiAlternatives(
            # title:
            "Password Reset for {}".format(site_full_name),
            # message:
            # email_plaintext_message,
            email_html_message,
            # from:
            "no-reply@{}".format(site_shortcut_name),
            # to:
            [reset_password_token.user.email],
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()
