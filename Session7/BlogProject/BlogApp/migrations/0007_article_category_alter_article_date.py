# Generated by Django 4.1.7 on 2023-04-03 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0006_category_remove_article_category_alter_article_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 3, 18, 46, 41, 621162)
            ),
        ),
    ]