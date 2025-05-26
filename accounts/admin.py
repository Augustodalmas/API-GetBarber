from django.contrib import admin
from accounts.models import usuarioVisitante, employee


@admin.register(usuarioVisitante)
class adminAgenda(admin.ModelAdmin):
    list_display = ('username', 'telefone')


@admin.register(employee)
class adminAgenda(admin.ModelAdmin):
    list_display = ('role', 'barbershop')
