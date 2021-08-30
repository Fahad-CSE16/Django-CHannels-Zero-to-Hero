from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import  Message

User = get_user_model()

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',]

class MessageSerializer(serializers.ModelSerializer):
    to_user = UserModelSerializer()
    from_user = UserModelSerializer()
    class Meta:
        model = Message
        fields = '__all__'