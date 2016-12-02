from .models import Question, Choice
from rest_framework import viewsets
from .serializers import QuestionSerializer, ChoiceSerializer
from django.http import HttpResponse
class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
	queryset = Choice.objects.all()
	serializer_class = ChoiceSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")