# Generated by Django 5.0.6 on 2024-09-12 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0031_productvariant_offer_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="address",
                to="userapp.address",
            ),
        ),
    ]
