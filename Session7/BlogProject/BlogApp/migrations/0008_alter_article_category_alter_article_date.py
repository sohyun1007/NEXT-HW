# Generated by Django 4.1.7 on 2023-04-03 09:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0007_article_category_alter_article_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="BlogApp.category",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 3, 18, 53, 12, 985720)
            ),
        ),
    ]
