from rest_framework import serializers
from onboarding.models import (
    ActivityType,
    Category,
    CategoryOffice,
    CategoryOfficeActivityAttempt,
    ConnectActivity,
    Office,
    PlayerCategoryOfficeProgress,
    PlayerOfficeProgress,
)


class ActivityTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityType
        fields = ['type_name']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description', ]


class OfficeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = ['id', 'office_name', 'office_imagen', ]


class PlayerOfficeProgressSerializer(serializers.ModelSerializer):
    office = OfficeSerializer(required=True)

    class Meta:
        model = PlayerOfficeProgress
        fields = ['id', 'office', ]


class CategoryOfficeSerializer(serializers.ModelSerializer):
    office = OfficeSerializer(required=True)
    category = CategorySerializer(required=True)

    class Meta:
        model = CategoryOffice
        fields = ['id', 'total_points_required', 'is_active', 'office', 'category']

class PlayerCategoryOfficeProgressSerializer(serializers.ModelSerializer):
    category_office = CategoryOfficeSerializer(required=True)

    class Meta:
        model = PlayerCategoryOfficeProgress
        fields = ['id', 'total_points', 'category_office', ]


class ConnectActivitySerializer(serializers.ModelSerializer):
    activity_type = ActivityTypeSerializer(required=True)

    class Meta:
        model = ConnectActivity
        fields = ['id', 'instructions', 'solution_code', 'activity_type', ]


class CategoryOfficeActivityAttempt(serializers.ModelSerializer):
    date = serializers.DateField(format='%m/%d/%Y', required=False)

    class Meta:
        model = CategoryOfficeActivityAttempt
        fields = ['date', 'result', 'player_category_office_progress', 'category_office_activity']
