from django.conf import settings
from django.db import models


class serviceBarbershop(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Barbershop(models.Model):
    name = models.CharField(max_length=255)
    CNPJ = models.CharField(max_length=18)
    andress = models.CharField(max_length=255)
    telephone = models.CharField(max_length=9)
    service = models.ManyToManyField(
        serviceBarbershop, related_name="Service_Barbershop")
    email = models.EmailField()
    is_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='is_owner')
    # photo = models.ImageField(
    #     upload_to='estabelecimentos/', null=True)
    description = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name
