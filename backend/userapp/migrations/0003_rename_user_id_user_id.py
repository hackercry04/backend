# Generated by Django 5.0.6 on 2024-08-31 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0002_user_role"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="user_id",
            new_name="id",
        ),
    ]
