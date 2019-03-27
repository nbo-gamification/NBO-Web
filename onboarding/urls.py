from django.conf.urls import (
    include,
    url,
)
from django.views.generic.base import RedirectView
from onboarding.views import (
    ActivitiesView,
    ActivityCreateView,
    PlayersCreateView,
    PlayersView,
)
from onboarding.rest_views import (
    CategoryOfficeActivitiesForCategoryOfficeView,
    GetAvailableOfficesForUserView,
    RegisterActivityAttemptView,
    SelectOfficeView,
)


rest_urls = [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(
        r'selectOffice/(?P<player_office_progress>\d+)$',
        SelectOfficeView.as_view(),
    ),
    url(
        r'getOfficesByPlayer/(?P<player_id>\d+)$',
        GetAvailableOfficesForUserView.as_view(),
    ),
    url(
        r'getActivitiesbyCategoryOffice/(?P<pk>\d+)$',
        CategoryOfficeActivitiesForCategoryOfficeView.as_view(),
    ),
    url(
        r'registerActivityAttempt/',
        RegisterActivityAttemptView.as_view(),
    ),
]

urlpatterns = [
    url(r'activities/$', ActivitiesView.as_view(), name='activities'),
    url(r'activities/create$', ActivityCreateView.as_view(), name='create_activity'),
    url(r'players/$', PlayersView.as_view(), name='players'),
    url(r'players/create$', PlayersCreateView.as_view(), name='create_player'),
    url(r'$', RedirectView.as_view(pattern_name='players'), name='root'),
]
