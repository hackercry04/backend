# Generated by Django 5.0.6 on 2024-09-02 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0010_remove_otp_is_expired"),
    ]

    operations = [
        migrations.AddField(
            model_name="otp",
            name="is_expire",
            field=models.BooleanField(default=True),
        ),
    ]
