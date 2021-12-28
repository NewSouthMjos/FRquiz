# Generated by Django 2.2.10 on 2021-12-28 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20211228_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_to_question', to='quiz.Question'),
        ),
    ]
