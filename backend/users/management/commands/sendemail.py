import os
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string
from django.dispatch import receiver
from django.core.mail import send_mail


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **kwargs):
        print("Sending test email...")
        self.send_formated_email()

    def send_formated_email(self):
        """
        Sends an email to the specififed email address.
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
            "current_user": "RJ",
            "username": "rogerjohnmorellizeller@gmail.com",
            "email": "rogerjohnmorellizeller@gmail.com",
            "site_name": site_shortcut_name,
            "site_domain": smtp_url,
        }

        # render email text

        email_html_message = render_to_string("user_test_email.html", context)

        # email_html_message = "test html message\n\n" + context['reset_password_url']
        # email_plaintext_message = "test text message\n\n" + context['reset_password_url']

        msg = EmailMultiAlternatives(
            # title:
            "Test email from {}".format(site_full_name),
            # message:
            # email_plaintext_message,
            email_html_message,
            # from:
            "no-reply@{}".format(smtp_url),
            # to:
            ["rogerjohnmorellizeller@gmail.com"],
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send(fail_silently=False)
        print("Email sent")

    def send_baisc_email(self):

        send_mail(
            "Subject here",
            "Here is the message.",
            "noreply@rzeller.net",
            ["rogerjohnmorellizeller@gmail.com"],
            fail_silently=False,
        )
