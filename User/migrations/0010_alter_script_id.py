# Generated by Django 3.2.10 on 2022-10-02 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20221001_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20221002201455', max_length=200, primary_key=True, serialize=False),
        ),
    ]
