# Generated by Django 4.2.3 on 2023-07-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='kind',
            field=models.TextField(default='Job Seeker'),
        ),
    ]
