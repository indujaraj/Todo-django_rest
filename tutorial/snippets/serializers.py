from rest_framework.serializers import ModelSerializer
from snippets.models import Todos

from django.contrib.auth.models import User
from rest_framework import serializers


class TodoSerializer(ModelSerializer):
    user=serializers.CharField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    class Meta:
        model = Todos
        fields = ['task_name','user','created_at']

    def create(self,validated_data):
        return Todos.objects.create(**validated_data,user=self.context['user'])


class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(email=validated_data['email'], username=validated_data['username'],
                                        password=validated_data['password'])


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
