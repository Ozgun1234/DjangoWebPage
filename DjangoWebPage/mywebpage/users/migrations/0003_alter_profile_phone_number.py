# Generated by Django 4.2.3 on 2023-07-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.TextField(default=None),
        ),
    ]
