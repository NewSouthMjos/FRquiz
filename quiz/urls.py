from django.urls import path

from .views import (
    CreateQuizView, WhoIsView, GetQuizDetailView, CreateQuizView,
    RUDQuizView
)



urlpatterns = [
    path('whois/', WhoIsView.as_view()),
    path('quiz/new', CreateQuizView.as_view()),
    path('quiz/<int:pk>', GetQuizDetailView.as_view()),
    path('quiz/<int:pk>/edit', RUDQuizView.as_view()),
    
    
]
