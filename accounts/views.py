from django.contrib.auth.views import LoginView
from accounts.forms import SignUpForm, Loginform
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import backends
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from accounts.tokens import account_activation_token
from accounts.models import NBOUser


class UserLoginView(LoginView):
    form_class = Loginform
    template_name = 'login.html'


class Registration(CreateView):
    form_class = SignUpForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('signup_email')
    domain = None

    def get_form_kwargs(self):
        kwargs = super(Registration, self).get_form_kwargs()
        kwargs.update({'domain': self.request.META['HTTP_HOST']})
        return kwargs


class RegistrationMail(TemplateView):
    template_name = 'simple_message.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['message'] = 'We send you an email with instructions for activating your account.'
        context['alert'] = 'info'
        context['login'] = False
        return self.render_to_response(context)


class ActivateAccount(TemplateView):

    template_name = "simple_message.html"

    def get_context_data(self, uidb64, token, **kwargs):
        context = super(ActivateAccount, self).get_context_data(**kwargs)
        message = None
        alert = None
        login = None
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            message = 'Your account is activated, you can now login.'
            alert = 'success'
            login = True
        elif user is not None and user.is_active:
            message = 'Your account is already activated.'
            alert = 'warning'
            login = True
        else:
            message = 'Activation link is invalid!.'
            alert = 'danger'
            login = False
        context['message'] = message
        context['alert'] = alert
        context['login'] = login
        return context

class EmailAuthBackend(backends.ModelBackend):

    def authenticate(self, request, username=None, password=None):
        try:
            user = NBOUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except NBOUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return NBOUser.objects.get(pk=user_id)
        except NBOUser.DoesNotExist:
            return None
