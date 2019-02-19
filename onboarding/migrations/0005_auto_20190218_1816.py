# Generated by Django 2.1.2 on 2019-02-18 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0004_categoryofficeactivityattempt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playercategoryofficeprogress',
            old_name='_total_points',
            new_name='total_points',
        ),
        migrations.RemoveField(
            model_name='playerofficeprogress',
            name='player_category_office_progress',
        ),
        migrations.AddField(
            model_name='playercategoryofficeprogress',
            name='player_office_progress',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='player_category_office_progress', to='onboarding.PlayerOfficeProgress'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoryoffice',
            name='total_points_required',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
