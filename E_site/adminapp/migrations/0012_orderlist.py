# Generated by Django 5.0.2 on 2024-05-07 08:54

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0011_producttable_product_img"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="orderList",
            fields=[
                ("orderId", models.AutoField(primary_key=True, serialize=False)),
                ("productquantity", models.IntegerField()),
                ("price", models.IntegerField()),
                (
                    "orderingTime",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "productId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminapp.producttable",
                    ),
                ),
                (
                    "userId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
