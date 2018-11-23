from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

from accounts.models import (
    NBOUser
)
from onboarding.onboarding_constants import USER_PLAYER



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

    def form_valid(self, form):
        valid = super().form_valid(form)
        new_player = form.instance
        players_group = Group.objects.get(name=USER_PLAYER)
        players_group.user_set.add(new_player)
        return valid
