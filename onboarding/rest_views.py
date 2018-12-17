from rest_framework import generics
from onboarding.rest_serializers import (
    PlayerCategoryOfficeProgressSerializer,
)
from onboarding.models import (
    Category,
    CategoryOffice,
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

# class ActivitiesForCategoryView(viewsets.ReadOnlyModelViewSet):
#     """
#     API endpoint that returns a list of activities to play in client
#     """
#     pass


# class RegisterActivityAttemptView(viewsets.ModelViewSet):
#     """
#     API endpoint that allows clients to register an activity attempt
#     """
#     pass
