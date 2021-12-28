from django.db import models
from django.db.models.deletion import CASCADE

class Quiz(models.Model):
    """
    Опрос для пользователей, содержит ссылки
    на конкретные вопросы
    """
    name = models.CharField(max_length=100, blank=False)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    description = models.TextField()


class Question(models.Model):
    """Вопрос, связанный с опросом"""
    quiz_id = models.ForeignKey(
        'Quiz',
        related_name='questions',
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=10)
    description = models.TextField()


class QuizReport(models.Model):
    """Сборник ответов на конкретную викторину"""
    quiz_id = models.ForeignKey(
        'Quiz',
        on_delete=models.CASCADE,
    )
    user_poiter_id = models.BigIntegerField(null=True, blank=True)


class Answer(models.Model):
    """Ответ на конкретный вопрос"""
    question_id = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE
    )
    quiz_report_id = models.ForeignKey(
        'QuizReport',
        on_delete=models.CASCADE
    )
    value = models.TextField()