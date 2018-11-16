from django.db import models

areas = [(1, 'TRBU'), (2, 'Briteling Experience'), (3, 'EDA'), ]


class Permissions(models.Model):
    permissiion = models.BooleanField(default=True)


class Role(models.Model):
    name = models.CharField(
        'name',
    )
    description = models.CharField(
        'description',
    )
    permission = models.ForeignKey(
        Permissions,
        on_delete=models.CASCADE,
    )


class PlayerUser(models.Model):

    first_name = models.CharField(
        'First name',
        max_length=30,
    )

    last_name = models.CharField(
        'Last name',
        max_length=30,
    )

    player_name = models.CharField(
        'Player name',
        max_length=30,
    )

    rol = models.IntegerField(
        'Area',
        default=1,
        choices=areas,
    )

    is_active = models.BooleanField(default=True)

    role = models.ForeignKey(Role)

    def __str__(self):
        return '{first} {last}'.format(
            first=self.first_name,
            last=self.last_name,
        )

    def rol_name(self):
        return areas[self.rol - 1][1]


class Office(models.Model):

    office_name = models.CharField(
        'Office',
        max=60,
    )


class Category(models.Model):

    category_name = models.CharField(
        'Office',
        max=60,
    )
    description = models.CharField(
        'description',
        max=60,
    )


class Activity(models.Model):
    description = models.CharField(
        'description',
        max=60,
    )
    default_points_reward = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category)


class CategoryOffice(models.Model):
    total_points_required = models.IntegerField()
    is_active = models.BooleanField(default=True)
    office = models.ForeignKey(Office)


class CategoryOfficeActivity(models.Model):
    _points_reward = models.IntegerField()
    is_active = models.BooleanField(default=True)
    activity = models.ForeignKey(Activity)
    category_office = models.ForeignKey(CategoryOffice)


class PlayerCategoryOfficeProgress(models.Model):
    _total_points = models.IntegerField()
    category_office = models.ForeignKey(CategoryOffice)


class PlayerOfficeProgress(models.Model):
    player = models.ForeignKey(PlayerUser)
    player_category_office_progress = models.ForeignKey(
        PlayerCategoryOfficeProgress,
    )


class ConnectActivity(Activity):
    instructions = models.CharField(
        'instructions',
        max=300,
    )
