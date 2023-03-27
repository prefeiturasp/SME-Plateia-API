from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('id', 'password', )


class BaseUserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = '__all__'


class SwaggerLoginSerializer(serializers.Serializer):
    rf = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'
