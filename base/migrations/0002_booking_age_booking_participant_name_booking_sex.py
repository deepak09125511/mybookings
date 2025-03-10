# Generated by Django 5.1.6 on 2025-02-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="age",
            field=models.PositiveIntegerField(default=18),
        ),
        migrations.AddField(
            model_name="booking",
            name="participant_name",
            field=models.CharField(default="unknown", max_length=255),
        ),
        migrations.AddField(
            model_name="booking",
            name="sex",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")],
                default="Male",
                max_length=10,
            ),
        ),
    ]
