from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from accounts.email_util import send_email
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    domain = None

    def __init__(self, *args, **kwargs):
        self.domain = kwargs.pop('domain')
        super(SignUpForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', )

    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        help_text=_("You must register using an Eventbrite domain email."),
    )

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'Invalid_domain': _("Please use an Eventbrite domain email."),
        'Email_taken': _("Email address already taken."),
    }

    def validate_email(self, email):
        return email.endswith('@eventbrite.com')

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        if any(self.errors):
            return
        email = cleaned_data.get("email")
        if not self.validate_email(email):
            raise forms.ValidationError(
                self.error_messages['Invalid_domain'],
                code='Invalid_domain',
            )
        username = cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(
                self.error_messages['Email_taken'],
                code='Email_taken',
            )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        send_email(user, self.domain)
        return user


class Loginform(AuthenticationForm):

    # username = forms.EmailField(
    #     label='Email',
    #     max_length=254,
    #     widget=forms.TextInput(attrs={'autofocus': True}),
    # )

    # def validate_email(self, email):
    #     return email.endswith('@eventbrite.com')

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

        # if not self.validate_email(user.email):
        #     raise forms.ValidationError(
        #         self.error_messages['Invalid_domain'],
        #         code='Invalid_domain',
        #     )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct username and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
        'Invalid_domain': _("Email must be part of Eventbrite domain."),
    }
