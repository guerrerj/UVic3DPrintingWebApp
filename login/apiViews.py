from .models import * 
from rest_framework import viewsets 
from .serializers import * 
from rest_framework.response import Response 

class CustomQuestionView(viewsets.ViewSet):
    def list(self, request, format=None):
        questions = []
        return response()

class ChoiceViewSet(viewsets.ModelViewSet):
    #authentication_classes 
    queryset = Choice.objects.all() 
    serializer_class = ChoiceSerializer 