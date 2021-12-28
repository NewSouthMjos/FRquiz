from rest_framework import serializers
from .models import Quiz, Question, QuizReport, Answer


class QuestionSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz_id', 'type', 'description', 'answers_choise']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'type', 'description', 'answers_choise']


class QuizSerializerDetail(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'start_date',
                  'end_date', 'description', 'questions']


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'description', 'start_date', 'end_date']
        extra_kwargs = {
            'start_date': {'required': False},
            'end_date': {'required': False},
        }
        validators = []

    def create(self, validated_data):
        return Quiz.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get(
            'start_date', instance.start_date
        )
        instance.end_date = validated_data.get(
            'end_date', instance.end_date
        )
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'value']


class QuizReportSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = QuizReport
        fields = ['id', 'quiz_id', 'user_id', 'answers']
        validators = []

    def create(self, validated_data):
        print('Creating ReportSerializer')
        answers_data = validated_data.pop('answers')
        quiz_report_obj = QuizReport.objects.create(**validated_data)
        for answer_data in answers_data:
            question_obj = answer_data.pop('question_id')

            # Make sure that question is exists and
            # is refer to same quiz:
            if question_obj.quiz_id != quiz_report_obj.quiz_id:
                message = f'The question_id #{question_obj.id} is refer to quiz#{question_obj.quiz_id.id}, but report is refered to quiz#{quiz_report_obj.quiz_id.id}!'
                raise serializers.ValidationError(message)

            Answer.objects.create(
                question_id=question_obj,
                quiz_report_id=quiz_report_obj,
                **answer_data
            )
        return quiz_report_obj


#Сериалайзеры для представления полного отчёта для пользователя
class AnswerFullSerializer(serializers.ModelSerializer):
    question_type = serializers.CharField(
        read_only=True, source="question_id.type"
    )
    question_description = serializers.CharField(
        read_only=True, source="question_id.description"
    )

    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'question_type',
                  'question_description', 'value']


class QuizReportFullSerializer(serializers.ModelSerializer):
    answers = AnswerFullSerializer(many=True, read_only=True)
    quiz_name = serializers.CharField(
        read_only=True, source="quiz_id.name"
    )
    quiz_name = serializers.CharField(
        read_only=True, source="quiz_id.name"
    )

    class Meta:
        model = QuizReport
        fields = ['id', 'quiz_id', 'user_id', 'answers']