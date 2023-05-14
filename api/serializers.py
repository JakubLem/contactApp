from rest_framework import serializers
from api import models


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 'status']
