# Generated by Django 4.0.4 on 2022-07-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0004_alter_users_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
