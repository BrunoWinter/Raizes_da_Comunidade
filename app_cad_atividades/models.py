from django.db import models
from django.contrib.auth.models import User
from httpx import request

from app_cad_usuario.views2 import user_login

class Atividade(models.Model):
    id= models.AutoField(primary_key=True)
    atividade = models.TextField(max_length=255)
    dt_atividadedb = models.DateField()
    usuario_id = models.CharField(max_length=100, default="admin")
    
    
    #id_especie = models.IntegerField()

    