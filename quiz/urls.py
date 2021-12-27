from django.urls import path

from .views import CreateQuizView, WhoIsView



urlpatterns = [
    path('whois/', WhoIsView.as_view())
]
