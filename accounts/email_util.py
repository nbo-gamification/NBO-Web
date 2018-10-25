from accounts.tokens import account_activation_token
from django.utils.http import (
    urlsafe_base64_encode,
)
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes


def send_email(user, domain):
        current_site = domain
        mail_subject = 'Activate your Eu-reporting account.'
        message = render_to_string(
            'registration/register_account_email.html',
            {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
        to_email = user.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
