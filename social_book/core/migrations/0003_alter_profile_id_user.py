# Generated by Django 5.1.3 on 2024-11-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(),
        ),
    ]
