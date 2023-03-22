from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('id', 'password', )


class BaseUserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = '__all__'


class SwaggerLogin(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'