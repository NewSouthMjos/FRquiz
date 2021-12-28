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
        fields = ['id', 'name', 'start_date', 'end_date', 'description', 'questions']


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
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question_id', 'quiz_report_id', 'value']

    def create(self, validated_data):
        print('Creating answer..')
        return Answer.objects.create(**validated_data)


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
            question_id = answer_data.pop('question_id')
            print(quiz_report_obj)
            Answer.objects.create(
                question_id=question_id,
                quiz_report_id=quiz_report_obj,
                **answer_data
            )
        return quiz_report_obj
