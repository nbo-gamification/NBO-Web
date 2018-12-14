from rest_framework import serializers
from onboarding.models import (
    Category,
    CategoryOffice,
    Office,
    PlayerCategoryOfficeProgress,
)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category_name', 'description', ]


class OfficeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = ['office_name', 'office_imagen', ]


class CategoryOfficeSerializer(serializers.ModelSerializer):
    office = OfficeSerializer(required=True)
    category = CategorySerializer(required=True)

    class Meta:
        model = CategoryOffice
        fields = ['total_points_required', 'is_active', 'office', 'category']

class PlayerCategoryOfficeProgressSerializer(serializers.ModelSerializer):
    category_office = CategoryOfficeSerializer(required=True)

    class Meta:
        model = PlayerCategoryOfficeProgress
        fields = ('_total_points', 'category_office',)
