from django.contrib.contenttypes.models import ContentType
from django.db import models, migrations
from onboarding.onboarding_constants import (
    activity_type_connect,
    DEFAULT_POINTS_REQUIRED_FOR_CATEGORY_OFFICE,
)


def apply_migration(apps, schema_editor):
    # Create Activity type Connect
    ActivityType = apps.get_model('onboarding', 'ActivityType')
    type_connect = ActivityType.objects.create(
        type_name=activity_type_connect,
    )

    # Create category Soccial
    Category = apps.get_model('onboarding', 'Category')
    category_soccial = Category.objects.create(
        category_name='Soccial',
        description='Relate with new people in the office.',
    )

    # Create office Mendoza
    Office = apps.get_model('onboarding', 'Office')
    office_mza = Office.objects.create(
        office_name='Mendoza',
        office_imagen='http://www.canal-la.com/noticias/images/c_eventbrite_020617_r.jpg',
    )

    # Create First Connect Activity
    ConnectActivity = apps.get_model('onboarding', 'ConnectActivity')
    connect_ct = ContentType.objects.get_for_model(ConnectActivity)  # Obtain type
    connect = ConnectActivity.objects.create(
        instructions='Find one of the NBO project developers and ask him/her his/her last name.',
        solution_code='Palma',
        activity_type=type_connect,
        is_active=True,
    )
    connect.polymorphic_ctype_id = connect_ct.id
    connect.category.add(category_soccial)
    connect.save()

    # Create CategoryOffice
    CategoryOffice = apps.get_model('onboarding', 'CategoryOffice')
    category_office = CategoryOffice.objects.create(
        total_points_required=DEFAULT_POINTS_REQUIRED_FOR_CATEGORY_OFFICE,
        is_active=True,
        office=office_mza,
        category=category_soccial,
    )

    # Create CategoryOfficeActivity
    CategoryOfficeActivity = apps.get_model('onboarding', 'CategoryOfficeActivity')
    CategoryOfficeActivity.objects.create(
        points_reward=2,
        is_active=True,
        activity=connect,
        category_office=category_office,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0005_auto_20190327_0916'),
    ]

    operations = [
        migrations.RunPython(apply_migration)
    ]
