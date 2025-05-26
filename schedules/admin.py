from django.contrib import admin
from .models import agenda


@admin.register(agenda)
class adminAgenda(admin.ModelAdmin):
    list_display = ('date', 'hours')
