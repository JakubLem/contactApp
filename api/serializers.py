from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from api import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 'status']

    def validate_status(self, value):
        r = self.context.get("request")
        if not r.user.is_staff and value != "NEW":
            raise ValidationError('You are not allowed to set this field.')
        return value
