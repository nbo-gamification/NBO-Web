from django.db import models

areas = [(1, 'TRBU'), (2, 'Briteling Experience'), (3, 'EDA'), ]


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

    def __str__(self):
        return '{first} {last}'.format(
            first=self.first_name,
            last=self.last_name,
        )

    def rol_name(self):
        return areas[self.rol - 1][1]
