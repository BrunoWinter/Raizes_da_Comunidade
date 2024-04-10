from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Horta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(null= True,max_length=50)
    descricao = models.TextField(null= True,max_length=150)

    def __str__(self):
        return f"self.nome - self.descricao"
