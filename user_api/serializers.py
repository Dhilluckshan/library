from rest_framework import serializers
from user_api.models import User
from services.models import Service
from services.serializers import ServiceSerializer

class UserSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    class Meta:
        model = User
        fields='__all__'
        
    