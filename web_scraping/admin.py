from django.contrib import admin

from .models import FormData, AvitoItem

@admin.register(FormData)
class FormAdmin(admin.ModelAdmin):
    list_display = ['form_url', 'categories']


@admin.register(AvitoItem)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'descriptions', 'url', 'price']

