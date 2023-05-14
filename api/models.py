from django.db import models


class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('APP', 'App Support'),
        ('PAY', 'Payment Support'),
        ('HR', 'HR/Jobs'),
        ('OTH', 'Other'),
    ]

    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('PRG', 'In progress'),
        ('RSL', 'Resolved'),
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=3, choices=SUBJECT_CHOICES)
    message = models.TextField(max_length=500)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='NEW')
