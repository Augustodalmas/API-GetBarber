from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class usuarioVisitante(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    historico = models.TextField(blank=True, null=True)
    # foto = models.ImageField(
    #     upload_to="perfil_imagens/", blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
