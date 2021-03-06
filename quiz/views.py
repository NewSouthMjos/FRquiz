import time

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import APIException


from .models import Quiz, Question, QuizReport
from .serializers import (
    QuizSerializerDetail, QuizSerializer, QuestionSerializerDetail,
    QuizReportSerializer, QuizReportFullSerializer
)


class AlreadyHasStartDateExeption(APIException):
    status_code = 403


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

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        try:
            quiz_obj = Quiz.objects.get(pk=self.kwargs['pk'])
            if quiz_obj.start_date is not None:
                message = f'Quiz #{quiz_obj.id} already has start date, so you cant modify this quiz!'
                raise AlreadyHasStartDateExeption(message)
        except Quiz.DoesNotExist:
            pass
            # let the default exeption handler handle this
        return self.update(request, *args, **kwargs)


class CreateQuestionView(generics.CreateAPIView):
    """Создание вопроса - для администратора"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = QuestionSerializerDetail
    queryset = Question.objects.all()


class RUDQuestionView(generics.RetrieveUpdateDestroyAPIView):
    """
    Чтение, обновление, удаление вопроса - для
    администратора
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = QuestionSerializerDetail
    queryset = Question.objects.all()


class GetQuizDetailView(APIView):
    """
    Отдаёт опрос вместе со всеми вопросами,
    принадлежащими данному опросу
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        serializer = QuizSerializerDetail(instance=quiz)
        return Response(serializer.data)


class GetAllActiveQuizView(APIView):
    """
    Отдаёт все опросы, активные на данный момент.
    Активные - значит текущее время лежит между
    start_date и end_date опроса.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        now_unix = int(time.time())
        quizs = Quiz.objects.filter(
            start_date__lt=now_unix,
            end_date__gt=now_unix
        )
        serializer = QuizSerializer(instance=quizs, many=True)
        return Response(serializer.data)


class GetQuizReportView(generics.ListAPIView):
    """
    Возвращает отчёт: детализацию пройденного опроса
    по id детализации
    """
    authentication_classes = []
    permission_classes = []

    serializer_class = QuizReportSerializer
    queryset = QuizReport.objects.all()

    def get_queryset(self):
        return self.queryset.filter(pk=self.kwargs['pk'])


class SaveQuizReportView(generics.ListCreateAPIView):
    """
    Сохраняет принятый в POST-запросе отчёт
    """
    authentication_classes = []
    permission_classes = []

    serializer_class = QuizReportSerializer
    queryset = QuizReport.objects.all()
    

class GetAllUserReportsView(APIView):
    """
    Возвращает все отчеты в подбробном виде, доступные
    для пользователя с переданным id
    """

    def get(self, request, user_id):
        reports = QuizReport.objects.filter(user_id=user_id)
        serializer = QuizReportFullSerializer(
            instance=reports, many=True
        )
        response_data = {
            "user_id": user_id,
            "quiz_reports": serializer.data
        }
        return Response(response_data)


class WhoIsView(APIView):
    """Запрос данных об аутентификации пользователя"""
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)