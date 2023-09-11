from rest_framework import serializers
from user_api.models import User
from services.models import Service
from services.serializers import ServiceSerializer


class UserSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('reg_number', 'password', 'faculty')

    def create(self, validated_data):
        user = User(reg_number=validated_data['reg_number'],
                    faculty=validated_data['faculty'], username=validated_data['reg_number'])
        user.set_password(validated_data['password'])
        user.save()
        return user
