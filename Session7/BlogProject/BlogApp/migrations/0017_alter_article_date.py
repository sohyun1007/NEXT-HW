# Generated by Django 4.1.7 on 2023-04-04 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0016_alter_article_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 14, 41, 15, 451235)
            ),
        ),
    ]
