# Generated by Django 2.2.10 on 2021-12-28 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20211228_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='quiz_report_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.QuizReport'),
        ),
        migrations.AlterField(
            model_name='quizreport',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_reports', to='quiz.Quiz'),
        ),
    ]
