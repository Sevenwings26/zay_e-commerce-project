# Generated by Django 5.0.2 on 2024-04-18 08:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("adminapp", "0006_producttable"),
    ]

    operations = [
        migrations.DeleteModel(
            name="productTable",
        ),
    ]