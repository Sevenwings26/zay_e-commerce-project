# Generated by Django 5.0.2 on 2024-04-18 08:10

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0007_delete_producttable"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="productCategory",
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
                ("cat_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="productTable",
            fields=[
                ("productId", models.IntegerField(primary_key=True, serialize=False)),
                ("product_name", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Electronics", "Electronics"),
                            ("Wears", "Wears"),
                            ("Lotions", "Lotions"),
                            ("Gym-kit", "Gym-kit"),
                        ],
                        max_length=100,
                    ),
                ),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("description", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]