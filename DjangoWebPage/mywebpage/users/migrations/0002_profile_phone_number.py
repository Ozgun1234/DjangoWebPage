# Generated by Django 4.2.3 on 2023-07-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
