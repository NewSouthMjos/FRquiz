# Generated by Django 2.2.10 on 2021-12-29 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20211228_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end_date',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start_date',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
