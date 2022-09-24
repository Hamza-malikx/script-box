# Generated by Django 3.2.10 on 2022-09-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_script_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20220924113238', max_length=200, primary_key=True, serialize=False),
        ),
    ]