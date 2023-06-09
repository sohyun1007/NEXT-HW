# Generated by Django 4.1.7 on 2023-04-08 11:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0023_rename_post_comment_article_alter_article_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 8, 20, 52, 4, 238783)
            ),
        ),
        migrations.CreateModel(
            name="Recomment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                (
                    "Comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recomments",
                        to="BlogApp.comment",
                    ),
                ),
            ],
        ),
    ]
