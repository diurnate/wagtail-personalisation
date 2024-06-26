# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_personalisation", "0009_auto_20170531_0428"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dayrule",
            options={"verbose_name": "Day Rule"},
        ),
        migrations.AlterModelOptions(
            name="devicerule",
            options={"verbose_name": "Device Rule"},
        ),
        migrations.AlterModelOptions(
            name="queryrule",
            options={"verbose_name": "Query Rule"},
        ),
        migrations.AlterModelOptions(
            name="referralrule",
            options={"verbose_name": "Referral Rule"},
        ),
        migrations.AlterModelOptions(
            name="timerule",
            options={"verbose_name": "Time Rule"},
        ),
        migrations.AlterModelOptions(
            name="userisloggedinrule",
            options={"verbose_name": "Logged in Rule"},
        ),
        migrations.AlterModelOptions(
            name="visitcountrule",
            options={"verbose_name": "Visit count Rule"},
        ),
        migrations.AlterField(
            model_name="referralrule",
            name="regex_string",
            field=models.TextField(
                verbose_name="Regular expression to match the referrer"
            ),
        ),
    ]
