from django.db import models, migrations
from onboarding.onboarding_constants import USER_GROUPS


def apply_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group in USER_GROUPS:
        Group.objects.create(
            name=group,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(apply_migration)
    ]
