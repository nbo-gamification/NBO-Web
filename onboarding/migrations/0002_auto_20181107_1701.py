# Generated by Django 2.1.2 on 2018-11-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playeruser',
            name='rol',
            field=models.IntegerField(choices=[(1, 'TRBU'), (2, 'Briteling Experience'), (3, 'EDA')], default=1),
        ),
        migrations.AlterField(
            model_name='playeruser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='playeruser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='playeruser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Last name'),
        ),
    ]
