# Generated by Django 4.2.3 on 2023-07-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_user_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_cv',
            field=models.FileField(default='default.png', upload_to='doc'),
        ),
    ]
