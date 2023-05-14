from django.shortcuts import render
from rest_framework import viewsets
from api import models, serializers


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


def contact(request):
    return render(request, 'contact.html')
