# Generated by Django 3.2.10 on 2022-09-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.CharField(default='20220907182941', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20220907182941', max_length=200, primary_key=True, serialize=False),
        ),
    ]
