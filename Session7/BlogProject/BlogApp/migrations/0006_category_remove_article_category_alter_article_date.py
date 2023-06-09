# Generated by Django 4.1.7 on 2023-04-03 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0005_alter_article_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category", models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="article",
            name="category",
        ),
        migrations.AlterField(
            model_name="article",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 3, 18, 34, 58, 305967)
            ),
        ),
    ]
