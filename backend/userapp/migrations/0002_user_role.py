# Generated by Django 5.0.6 on 2024-08-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("admin", "admin"), ("user", "user")],
                default="admin",
                max_length=20,
            ),
        ),
    ]
