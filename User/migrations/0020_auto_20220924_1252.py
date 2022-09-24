# Generated by Django 3.2.7 on 2022-09-24 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_auto_20220924_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='favcontent',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.content'),
        ),
        migrations.AlterField(
            model_name='favcontent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20220924125238', max_length=200, primary_key=True, serialize=False),
        ),
    ]