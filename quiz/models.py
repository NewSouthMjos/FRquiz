from django.db import models
from django.db.models.deletion import CASCADE

class Quiz(models.Model):
    """
    Опрос для пользователей, содержит ссылки
    на конкретные вопросы
    """
    name = models.CharField(max_length=100, blank=False)
    start_date = models.BigIntegerField(null=True, blank=True)
    end_date = models.BigIntegerField(null=True, blank=True)
    description = models.TextField()


class Question(models.Model):
    """Вопрос, связанный с опросом"""
    quiz_id = models.ForeignKey(
        'Quiz',
        related_name='questions',
        on_delete=models.CASCADE,
    )

    # type should be one of values: text, choise, multichoise
    type = models.CharField(max_length=11)
    
    description = models.TextField()
    answers_choise = models.TextField(null=True)


class QuizReport(models.Model):
    """Сборник ответов на конкретный опрос"""
    quiz_id = models.ForeignKey(
        'Quiz',
        related_name='quiz_reports',
        on_delete=models.CASCADE,
    )
    user_id = models.BigIntegerField(null=True, blank=True)


class Answer(models.Model):
    """Ответ на конкретный вопрос"""
    question_id = models.ForeignKey(
        'Question',
        related_name='answers_to_question',
        on_delete=models.CASCADE
    )
    quiz_report_id = models.ForeignKey(
        'QuizReport',
        related_name='answers',
        on_delete=models.CASCADE
    )
    value = models.TextField()