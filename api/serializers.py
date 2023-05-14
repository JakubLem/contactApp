from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api import models


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 'status']

    def validate_status(self, value):
        r = self.context.get("request")
        if not r.user.is_staff and value != "NEW":
            raise ValidationError('You are not allowed to set this field.')
        return value
