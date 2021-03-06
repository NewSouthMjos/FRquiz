from django.urls import path

from .views import (
    CreateQuizView, WhoIsView, GetQuizDetailView, CreateQuizView,
    RUDQuizView, CreateQuestionView, RUDQuestionView,
    GetAllActiveQuizView, GetQuizReportView, SaveQuizReportView,
    GetAllUserReportsView,
)



urlpatterns = [
    path('whois/', WhoIsView.as_view()),
    path('quiz/new', CreateQuizView.as_view()),
    path('quiz/<int:pk>', GetQuizDetailView.as_view()),
    path('quiz/<int:pk>/edit', RUDQuizView.as_view()),

    path('question/new', CreateQuestionView.as_view()),
    path('question/<int:pk>/edit', RUDQuestionView.as_view()),

    path('quiz/getallactive', GetAllActiveQuizView.as_view()),

    # Reports
    path('report/<int:pk>', GetQuizReportView.as_view()),
    path('make_report', SaveQuizReportView.as_view()),
    path('get_all_user_reports/<int:user_id>', GetAllUserReportsView.as_view()),
    
]
