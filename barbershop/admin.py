from django.contrib import admin
from .models import Barbershop


@admin.register(Barbershop)
class adminAgenda(admin.ModelAdmin):
    list_display = ('name', 'CNPJ')
