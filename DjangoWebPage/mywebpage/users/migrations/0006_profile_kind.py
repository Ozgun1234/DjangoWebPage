# Generated by Django 4.2.3 on 2023-07-14 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_user_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='kind',
            field=models.IntegerField(default=0),
        ),
    ]