# Generated by Django 4.1.4 on 2023-01-04 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0012_comment_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="user",
        ),
    ]
