# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_personalisation", "0002_auto_20161205_1623"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="queryrule",
            name="query_parameter",
        ),
        migrations.RemoveField(
            model_name="queryrule",
            name="query_value",
        ),
        migrations.AddField(
            model_name="queryrule",
            name="parameter",
            field=models.SlugField(
                default="test",
                max_length=20,
                verbose_name="The query parameter to search for",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="queryrule",
            name="value",
            field=models.SlugField(
                default="test",
                max_length=20,
                verbose_name="The value of the parameter to match",
            ),
            preserve_default=False,
        ),
    ]
