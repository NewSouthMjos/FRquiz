# Generated by Django 2.2.10 on 2021-12-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_answer_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]