from django.contrib import admin
from accounts.models import usuarioVisitante


class usuarioVisitanteAdministracao(admin.ModelAdmin):
    list_display = ('username', 'telefone')


admin.site.register(usuarioVisitante, usuarioVisitanteAdministracao)
