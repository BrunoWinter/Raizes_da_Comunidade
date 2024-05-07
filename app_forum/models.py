from django.db import models
from django.contrib.auth.models import User

class Topico(models.Model):
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    comentario = models.TextField(max_length=300)
