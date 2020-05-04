# Generated by Django 3.0.5 on 2020-05-03 16:12

from django.db import migrations
from django.db import models

import project.utils.xdatetime


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.TextField(blank=True, null=True)),
                ("link", models.TextField(blank=True, null=True)),
                ("linkName", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("gallery", models.TextField(blank=True, null=True)),
                ("sponsor", models.TextField(blank=True, null=True)),
                ("sponsorLogo", models.TextField(blank=True, null=True)),
                (
                    "started_at",
                    models.DateField(default=project.utils.xdatetime.utcnow),
                ),
                ("finished_at", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
