from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from onboarding.models import (
    PlayerUser
)


class PlayersView(LoginRequiredMixin, ListView):
    template_name = "players.html"
    queryset = PlayerUser.objects.all().order_by('-id')
    context_object_name = 'players'
    paginate_by = 5

class PlayersCreateView(LoginRequiredMixin, CreateView):
    model = PlayerUser
    fields = ['first_name', 'last_name', 'player_name', 'rol']
    template_name = 'create_player.html'
    success_url = 'players'
