# Generated by Django 5.0.2 on 2024-04-16 08:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0003_producttable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="producttable",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]