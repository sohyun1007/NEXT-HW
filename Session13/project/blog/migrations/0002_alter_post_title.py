# Generated by Django 4.2 on 2023-05-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=50, verbose_name="is it right?"),
        ),
    ]