# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:28
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0001_initial"),
        ("wagtail_personalisation", "0010_auto_20170531_1101"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalisablePageMetadata",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_segmented", models.BooleanField(default=False)),
                (
                    "canonical_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="personalisable_canonical_metadata",
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "segment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="page_metadata",
                        to="wagtail_personalisation.Segment",
                    ),
                ),
                (
                    "variant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="_personalisable_page_metadata",
                        to="wagtailcore.Page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
