from django.contrib.auth.views import LoginView
from accounts.forms import SignUpForm, Loginform
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import backends
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from accounts.tokens import account_activation_token
from accounts.models import NBOUser
import requests
from django.conf import settings
from django.shortcuts import render
from accounts.serializers import SmallNBOUserSerializer


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



def sandwich(request, id=1):
    sandwich_data = {}
    # The magic happens in our _react_render helper function
    return _react_render({'sandwich': sandwich_data}, request)


def _react_render(content, request):
    # Let's grab our user's info if she has any
    if request.user.is_authenticated:
        serializer = SmallNBOUserSerializer(request.user)
        user = serializer.data
    else:
        user = {}

    # Here's what we've got so far
    render_assets = {
        # 'url': request.path_info,
        'url': '/',
        'user': user
    }
    # Now we add the sandwich. We use the Dict#update method so that the
    # key could be anything, like pizza or cake or burger.
    render_assets.update(content)

    try:
        # All right, let's send it! Note that we set the content type to json.
        res = requests.post(settings.RENDER_SERVER_BASE_URL + '/render',
                            json=render_assets,
                            headers={'content_type': 'application/json'})
        rendered_payload = res.json()
    except Exception as e:
        print (e)
    # Beautiful! Let's render this stuff into our base template
    print (rendered_payload)
    return render(request, 'login.html', rendered_payload)
