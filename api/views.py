from django.shortcuts import render
from rest_framework import viewsets
from api import models, serializers


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


def contact(request):
    return render(request, 'contact.html')
