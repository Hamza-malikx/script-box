# Generated by Django 3.2.7 on 2022-09-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_auto_20220911_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
