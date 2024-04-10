from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Horta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(null= False, max_length=50)
    descricao = models.TextField(null= False, max_length=150)

    def __str__(self):
        return f"self.nome"
    
    
class Cultura(models.Model):
    horta = models.ForeignKey(Horta, on_delete=models.CASCADE)
    nome = models.CharField(null= False, max_length=50)
    descricao = models.TextField(null= False, max_length=150)
    tipo = models.CharField(null= False, max_length=50)
    
class Plantio(models.Model):
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)
    dt_plantio = models.DateField(null=False)
    ultima_atv = models.DateField(null=True)
    descricao_atv = models.TextField(null= True)
    

