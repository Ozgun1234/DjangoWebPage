# Generated by Django 4.2.3 on 2023-07-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='I am new'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='kind',
            field=models.IntegerField(default='J'),
        ),
    ]
