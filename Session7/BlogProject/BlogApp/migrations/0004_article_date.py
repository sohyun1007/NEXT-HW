# Generated by Django 4.1.7 on 2023-04-03 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BlogApp", "0003_article_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="date",
            field=models.DateTimeField(null=True),
        ),
    ]