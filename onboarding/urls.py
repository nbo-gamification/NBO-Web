from django.conf.urls import (
    include,
    url,
)
from django.views.generic.base import RedirectView
from onboarding.views import (
    HomeView
)

urlpatterns = [
    url(r'home/$', HomeView.as_view(), name='home'),
    url(r'', RedirectView.as_view(pattern_name='home'), name='root'),
]
