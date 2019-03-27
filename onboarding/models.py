from django.db import models
from accounts.models import NBOUser
from polymorphic.models import PolymorphicModel


class Office(models.Model):

    office_name = models.CharField(
        'Office',
        max_length=60,
    )
    office_imagen = models.CharField(
        'office_imagen',
        max_length=350,
    )

    def __str__(self):
        return self.office_name


class Briteling(models.Model):
    name = models.CharField(
        'briteling_name',
        max_length=60,
    )
    position = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
    )
    briteling_image = models.CharField(
        'briteling_image',
        max_length=350,
    )


class Category(models.Model):

    category_name = models.CharField(
        'category_name',
        max_length=60,
    )
    description = models.CharField(
        'description',
        max_length=350,
    )

    def __str__(self):
        return self.category_name

class ActivityType(models.Model):
    type_name = models.CharField(
        'type_name',
        max_length=60,
    )

    def __str__(self):
        return self.type_name


class Activity(PolymorphicModel):
    is_active = models.BooleanField(default=True)
    category = models.ManyToManyField(
        Category,
        blank=True,
    )
    activity_type = models.ForeignKey(
        ActivityType,
        on_delete=models.CASCADE,
        blank=True,
        default=None,
    )


class CategoryOffice(models.Model):
    total_points_required = models.IntegerField(
        blank=True,
        default=0,
    )
    is_active = models.BooleanField(default=True)
    office = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )


class CategoryOfficeActivity(models.Model):
    points_reward = models.IntegerField()
    is_active = models.BooleanField(default=True)
    activity = models.ForeignKey(
        Activity,
        on_delete=models.CASCADE,
    )
    category_office = models.ForeignKey(
        CategoryOffice,
        on_delete=models.CASCADE,
    )

class PlayerOfficeProgress(models.Model):
    player = models.ForeignKey(
        NBOUser,
        on_delete=models.CASCADE,
    )
    office = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
    )


class PlayerCategoryOfficeProgress(models.Model):
    total_points = models.IntegerField(
        default=0,
    )
    category_office = models.ForeignKey(
        CategoryOffice,
        on_delete=models.CASCADE,
    )
    player_office_progress = models.ForeignKey(
        PlayerOfficeProgress,
        on_delete=models.CASCADE,
        related_name='player_category_office_progress',
    )


class ConnectActivity(Activity):
    instructions = models.CharField(
        'Activity_instructions',
        max_length=300,
    )
    solution_code = models.CharField(
        'solution_code',
        max_length=60,
    )

    def get_description(self):
        return self.instructions

class CategoryOfficeActivityAttempt(models.Model):
    date = models.DateField(
        auto_now_add=True,
    )
    result = models.BooleanField(
        default=False
    )
    player_category_office_progress = models.ForeignKey(
        PlayerCategoryOfficeProgress,
        on_delete=models.CASCADE,
    )
    category_office_activity = models.ForeignKey(
        CategoryOfficeActivity,
        on_delete=models.CASCADE,
    )
