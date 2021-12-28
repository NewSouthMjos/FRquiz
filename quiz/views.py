from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.parsers import JSONParser

from .models import Quiz
from .serializers import QuizSerializerDetail, QuizSerializer


class CreateQuizView(generics.CreateAPIView):
    """Создание опросника - для администратора"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RUDQuizView(generics.RetrieveUpdateDestroyAPIView):
    """
    Чтение, обновление, удаление опросника - для
    администратора
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class GetQuizDetailView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        serializer = QuizSerializerDetail(instance=quiz)
        return Response(serializer.data)


class WhoIsView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)