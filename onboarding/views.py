from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect

from accounts.models import (
    NBOUser,
)
from onboarding.forms import (
    CategoryOfficeActivityForm,
    ConnectForm,
    OfficeForm
)
from onboarding.models import (
    Activity,
    ActivityType,
    Category,
    CategoryOffice,
    CategoryOfficeActivity,
    ConnectActivity,
    Office,
    PlayerOfficeProgress,
)
from onboarding.onboarding_constants import (
    activity_type_connect,
    DEFAULT_POINTS_REQUIRED_FOR_CATEGORY_OFFICE,
    USER_PLAYER,
)


class PlayersView(LoginRequiredMixin, ListView):
    template_name = "players.html"
    queryset = NBOUser.objects.filter(groups__name=USER_PLAYER).order_by('-id')
    context_object_name = 'players'
    paginate_by = 5


class PlayersCreateView(LoginRequiredMixin, CreateView):
    model = NBOUser
    fields = ['email', 'password', 'first_name', 'last_name', ]
    template_name = 'create_player.html'
    success_url = 'players'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = self.get_context_data()
        context['office_form'] = OfficeForm
        return self.render_to_response(context)

    def form_valid(self, form):
        valid = super().form_valid(form)
        new_player = form.instance
        players_group = Group.objects.get(name=USER_PLAYER)
        players_group.user_set.add(new_player)
        self._create_player_progress(new_player)
        return valid

    def _create_player_progress(self, new_player):
        # Creates a progres for every office selected for this player
        offices = Office.objects.filter(pk=self.request.POST.get('office'))
        for office in offices:
            PlayerOfficeProgress.objects.create(
                office=office,
                player=new_player,
            )


class ActivitiesView(LoginRequiredMixin, ListView):
    template_name = "activities.html"
    queryset = CategoryOfficeActivity.objects.all().order_by('-id')
    context_object_name = 'category_activities'
    paginate_by = 6


class ActivityCreateView(LoginRequiredMixin, CreateView):
    model = Activity
    fields = [
        'activity_type',
        'category',
    ]
    template_name = 'create_activity.html'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = self.get_context_data()
        context['activity_form'] = ConnectForm
        context['office_activity_form'] = CategoryOfficeActivityForm
        context['office_form'] = OfficeForm
        return self.render_to_response(context)

    def form_valid(self, form):
        new_activity = form.instance
        if new_activity.activity_type.type_name == activity_type_connect:
            self.create_connect_activity(self.request.POST)
        return HttpResponseRedirect('activities')

    def create_connect_activity(self, request):
        category = Category.objects.get(pk=request['category'])
        activity_type = ActivityType.objects.get(pk=request['activity_type'])
        office = Office.objects.get(pk=request['office'])

        new_activity = ConnectActivity.objects.create(
            instructions=request['instructions'],
            solution_code=request['solution_code'],
            activity_type=activity_type,
        )
        new_activity.category.add(category)

        category_office, _ = CategoryOffice.objects.get_or_create(
            office=office,
            category=category,
            defaults={
                'total_points_required': DEFAULT_POINTS_REQUIRED_FOR_CATEGORY_OFFICE,
            },
        )

        CategoryOfficeActivity.objects.create(
            activity=new_activity,
            category_office=category_office,
            points_reward=request['points_reward']
        )
