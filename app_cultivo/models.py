from django.db import models

class Cultivo(models.Model):
    foto = models.TextField(max_length=300)
    nome = models.CharField(max_length=50)
    processo = models.TextField(max_length=300)
    nome_cientifico = models.TextField(max_length=300)
    
