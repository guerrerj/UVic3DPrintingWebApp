from .models import * 
from rest_framework import serializers 

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice 
        