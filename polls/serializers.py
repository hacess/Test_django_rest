from rest_framework import (
	serializers, 
	viewsets
	)
from .models import Question, Choice



class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ('choice_text','votes')



class QuestionSerializer(serializers.ModelSerializer):
	choices=ChoiceSerializer(many=True,read_only=True)

	class Meta:
		model = Question
		fields = ('question_text','pub_date','choices')
