# Generated by Django 2.2.10 on 2021-12-28 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20211228_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizreport',
            old_name='user_poiter_id',
            new_name='user_id',
        ),
    ]
