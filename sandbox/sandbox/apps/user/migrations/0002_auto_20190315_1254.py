# Generated by Django 2.1.7 on 2019-03-15 12:54

from django.db import migrations

import sandbox.apps.user.models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", sandbox.apps.user.models.UserManager()),
            ],
        ),
    ]
