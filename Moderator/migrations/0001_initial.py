# Generated by Django 3.2.10 on 2022-09-24 10:42

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0003_alter_script_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('User.user',),
            managers=[
                ('moderator', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
