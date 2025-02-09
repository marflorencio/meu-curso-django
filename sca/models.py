from django.conf import settings
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    SITUACAO = {"A": "Ativo", "I" : "Inativo", "S": "Suspenso", "O":"outro",}
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=75)
    situacao = models.CharField(max_length=1, choices=SITUACAO, default="A")
    data_alteracao = models.DateTimeField('data alteração')

    def salvar(self):
        self.data_alteracao = timezone.now()
        self.save()