# Generated by Django 3.2.7 on 2022-09-06 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20220906_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='user',
        ),
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.CharField(default='20220906212516', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='script',
            name='id',
            field=models.CharField(default='20220906212516', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='PrivateKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('privateKey', models.TextField()),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.script')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]