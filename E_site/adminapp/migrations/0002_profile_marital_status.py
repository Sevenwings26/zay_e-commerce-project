# Generated by Django 5.0.2 on 2024-03-05 09:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="marital_status",
            field=models.CharField(
                choices=[
                    ("Single", "Single"),
                    ("Married", "Married"),
                    ("Divorced", "Divorced"),
                    ("Complicated", "Complicated"),
                ],
                default="DEFAULT VALUE",
                max_length=20,
            ),
        ),
    ]
