# Generated by Django 3.2.7 on 2022-09-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0013_auto_20220907_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.CharField(default='20220907215835', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='privatekey',
            name='privateKey',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20220907215835', max_length=200, primary_key=True, serialize=False),
        ),
    ]