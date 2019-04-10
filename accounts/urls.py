from django.conf.urls import include, url
from accounts.views import (
    Registration,
    UserLoginView,
    ActivateAccount,
    RegistrationMail,
)
from accounts.react_views import (
    ReactUserLoginView,
)

urlpatterns = [
    url(r'^login/$', UserLoginView.as_view(), name='login'),
    url(r'^signup/$', Registration.as_view(), name='signup'),
    url(r'^signup/email$', RegistrationMail.as_view(), name='signup_email'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        ActivateAccount.as_view(), name='activate_account'),
    url(r'^', include('django.contrib.auth.urls')),
]
