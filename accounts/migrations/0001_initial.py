# Generated by Django 2.2.10 on 2021-12-27 12:36

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('api_key', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]
