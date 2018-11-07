from django.conf.urls import (
    include,
    url,
)
from django.views.generic.base import RedirectView
from onboarding.views import (
    PlayersCreateView,
    PlayersView,
)

urlpatterns = [
    url(r'players/$', PlayersView.as_view(), name='players'),
    url(r'players/create$', PlayersCreateView.as_view(), name='create_player'),
    url(r'$', RedirectView.as_view(pattern_name='players'), name='root'),
]
