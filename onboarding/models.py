from django.db import models
from accounts.models import NBOUser


class Office(models.Model):

    office_name = models.CharField(
        'Office',
        max_length=60,
    )
    imagen = models.CharField(
        'imagen',
        max_length=350,
    )

class Category(models.Model):

    category_name = models.CharField(
        'Office',
        max_length=60,
    )
    description = models.CharField(
        'description',
        max_length=60,
    )


class Activity(models.Model):
    description = models.CharField(
        'description',
        max_length=60,
    )
    default_points_reward = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )


class CategoryOffice(models.Model):
    total_points_required = models.IntegerField()
    is_active = models.BooleanField(default=True)
    office = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
    )


class CategoryOfficeActivity(models.Model):
    _points_reward = models.IntegerField()
    is_active = models.BooleanField(default=True)
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
    )
    category_office = models.ForeignKey(
        CategoryOffice,
        on_delete=models.CASCADE,
    )


class PlayerCategoryOfficeProgress(models.Model):
    _total_points = models.IntegerField()
    category_office = models.ForeignKey(
        CategoryOffice,
        on_delete=models.CASCADE,
    )


class PlayerOfficeProgress(models.Model):
    player = models.ForeignKey(
        NBOUser,
        on_delete=models.CASCADE,
    )
    player_category_office_progress = models.ForeignKey(
        PlayerCategoryOfficeProgress,
        on_delete=models.CASCADE,
    )


class ConnectActivity(Activity):
    instructions = models.CharField(
        'instructions',
        max_length=300,
    )
