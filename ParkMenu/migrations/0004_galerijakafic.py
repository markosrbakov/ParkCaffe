# Generated by Django 5.1.6 on 2025-02-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ParkMenu", "0003_event_reservations_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalerijaKafic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="gallery/"),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True, null=True, upload_to="gallery/videos/"
                    ),
                ),
            ],
        ),
    ]
