# Generated by Django 3.2.10 on 2022-09-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_script_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20220924155130', max_length=200, primary_key=True, serialize=False),
        ),
    ]
