# Generated by Django 4.2 on 2023-04-28 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("LoginApp", "0004_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="code",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="codes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
