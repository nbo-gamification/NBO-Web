from django.shortcuts import get_object_or_404

from rest_framework import generics
from onboarding.rest_serializers import (
    CategoryOfficeActivityAttempt,
    ConnectActivitySerializer,
    PlayerCategoryOfficeProgressSerializer,
    PlayerOfficeProgressSerializer,
)
from onboarding.models import (
    Category,
    CategoryOffice,
    ConnectActivity,
    PlayerOfficeProgress,
    PlayerCategoryOfficeProgress,
)
from onboarding.onboarding_constants import DEFAULT_POINTS_REQUIRED_FOR_CATEGORY_OFFICE


class SelectOfficeView(generics.RetrieveAPIView):
    """
    API endpoint that returns player progress and categories he/she can play
    """
    lookup_field = 'playerofficeprogress'
    serializer_class = PlayerCategoryOfficeProgressSerializer

    def get_queryset(self):
        id_player_office_progress = int(self.request.parser_context.get('kwargs').get('playerofficeprogress'))
        self._validate_asigned_progress(id_player_office_progress)
        queryset = PlayerCategoryOfficeProgress.objects.filter(
            playerofficeprogress__player_category_office_progress=id_player_office_progress,
        )
        return queryset

    def _validate_asigned_progress(self, id_player_office_progress):
        player_progress = PlayerOfficeProgress.objects.get(pk=id_player_office_progress)
        categories = Category.objects.all()
        if player_progress.player_category_office_progress is None:
            for category in categories:
                category_office = CategoryOffice.objects.create(
                    total_points_required=DEFAULT_POINTS_REQUIRED_FOR_CATEGORY_OFFICE,
                    office=player_progress.office,
                    category=category,
                )
                player_category_office_progress = PlayerCategoryOfficeProgress.objects.create(
                    category_office=category_office,
                )
                player_progress.player_category_office_progress = player_category_office_progress
            player_progress.save()


class GetAvailableOfficesForUserView(generics.RetrieveAPIView):
    """
    API endpoint that return all posible offices an user can select
    """
    lookup_field = 'player_id'
    serializer_class = PlayerOfficeProgressSerializer

    def get_queryset(self):
        id_player = int(self.request.parser_context.get('kwargs').get('player_id'))
        queryset = PlayerOfficeProgress.objects.filter(
            player_id=id_player,
        )
        return queryset


class ActivitiesForCategoryOfficeView(generics.ListAPIView):
    """
    API endpoint that returns a list of activities to play in client
    """
    serializer_class = ConnectActivitySerializer

    def get_queryset(self):
        category_office_id = int(self.request.parser_context.get('kwargs').get('pk'))
        queryset = ConnectActivity.objects.filter(
            categoryofficeactivity__category_office_id=category_office_id
        )
        queryset.exclude(categoryofficeactivity__categoryofficeactivityattempt__isnull=False)
        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset,)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


class RegisterActivityAttemptView(generics.CreateAPIView):
    """
    API endpoint that allows clients to register an activity attempt
    """
    serializer_class = CategoryOfficeActivityAttempt
