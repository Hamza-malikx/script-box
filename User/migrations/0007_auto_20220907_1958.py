# Generated by Django 3.2.7 on 2022-09-07 14:58

import User.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20220907_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.CharField(default='20220907195800', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='privatekey',
            name='privateKey',
            field=models.JSONField(default=User.models.contact_default, verbose_name='privateKey'),
        ),
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20220907195800', max_length=200, primary_key=True, serialize=False),
        ),
    ]