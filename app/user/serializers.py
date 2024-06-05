from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from app.user.models import User
from utils import Responder, FriendshipStatus


class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserLoginSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    
    def validate(self, attrs):
        user = User.objects.get_by_credential(**attrs)
        if not user:
            Responder.error(102)
        return {"user": user}

    def create(self, attrs):
        user = attrs['user']
        return user.login()


class CurrentUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "name", "email"]


class UserDetailSerializer(serializers.ModelSerializer):
    friend_status = serializers.ChoiceField(FriendshipStatus.choices)
    
    class Meta:
        model = User
        fields = ["id", "name", "email", "friend_status"]
