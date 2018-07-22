from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('user_id', 'about', 'birthday', 'country', 'photo')
