# Generated by Django 4.1.7 on 2023-04-08 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0024_alter_article_date_recomment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recomment",
            old_name="Comment",
            new_name="comment",
        ),
        migrations.AlterField(
            model_name="article",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 8, 20, 55, 1, 158070)
            ),
        ),
    ]
