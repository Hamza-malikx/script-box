# Generated by Django 3.2.10 on 2022-09-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20220907_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.CharField(default='20220907183325', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20220907183326', max_length=200, primary_key=True, serialize=False),
        ),
    ]
