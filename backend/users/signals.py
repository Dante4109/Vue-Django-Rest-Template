from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.dispatch import receiver
from .models import CustomUser, UserEmailVerification
from .serializers import UserSerializer
import uuid
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import os


@receiver(post_save, sender=CustomUser)
def post_save_create_profile(sender, instance, created, **kwargs):
    print("New user created")
    if created:
        # Example for User Verification Token Generation
        v_token = uuid.uuid4()
        new_verification = UserEmailVerification.objects.create(
            user_id=instance.id, verification_token=v_token
        )

        # Sending the Email
        # replace with environment file eventually
        site_url = os.getenv("SITE_URL")
        site_full_name = os.getenv("SITE_FULL_NAME")
        site_shortcut_name = os.getenv("SITE_SHORTCUT_NAME")
        smtp_url = os.getenv("SMTP_URL")

        context = {
            "email": instance.email,
            "email_verification_url": "{}/email_verification/{}".format(
                site_url, v_token
            ),
            "site_name": site_shortcut_name,
            "site_domain": smtp_url,
        }

        email_html_message = render_to_string("user_email_verification.html", context)

        print(f"no-reply@{site_shortcut_name}")

        msg = EmailMultiAlternatives(
            # title:
            "Email Verification for {}".format(site_full_name),
            # message:
            # email_plaintext_message,
            email_html_message,
            # from:
            (f"no-reply@{smtp_url}"),
            # to:
            [instance.email],
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()

    else:
        try:
            profile = get_object_or_404(profiles, id=instance.profile_id)
            profile.name = instance.name
            profile.save()
        except:
            # An unhandled Error has occured
            pass
