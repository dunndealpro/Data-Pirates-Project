# Generated by Django 4.1.4 on 2023-01-03 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0006_alter_chore_id_alter_comment_id_alter_supply_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="supply",
            name="qty",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
