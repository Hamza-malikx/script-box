# Generated by Django 3.2.10 on 2022-09-05 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.CharField(default='20220905165050', max_length=200, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=600)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_universal', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('features', models.TextField(blank=True, null=True)),
                ('tag', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Paid', 'Paid'), ('Free', 'Free')], max_length=50, null=True)),
                ('privacy', models.CharField(choices=[('Public', 'Public'), ('Unlisted', 'Unlisted'), ('Private', 'Private')], max_length=50, null=True)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('num_reviews', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.content')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
