# Generated by Django 4.2 on 2023-05-02 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ("-update_dt", "author"),
                "verbose_name": "MyPost",
                "verbose_name_plural": "MyPosts",
            },
        ),
    ]
