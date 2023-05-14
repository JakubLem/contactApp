from django.contrib import admin
from api.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status')
    list_editable = ('status',)