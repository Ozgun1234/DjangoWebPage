# Generated by Django 4.2.3 on 2023-07-14 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_cv',
            field=models.FileField(default=None, upload_to='doc'),
            preserve_default=False,
        ),
    ]
