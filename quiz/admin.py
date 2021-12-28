from django.contrib import admin
from .models import Quiz, Question, QuizReport, Answer

admin.site.register([
    Quiz,
    Question,
    QuizReport,
    Answer,
])
