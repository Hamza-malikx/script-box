# Generated by Django 3.2.7 on 2022-09-11 11:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_alter_content_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
