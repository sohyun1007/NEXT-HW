# Generated by Django 4.2 on 2023-05-03 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0002_alter_profile_options_alter_profile_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={
                "verbose_name": "User_Profile",
                "verbose_name_plural": "User_Profiles",
            },
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
