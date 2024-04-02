from django.db import models

class Atividade(models.Model):
    id= models.AutoField(primary_key=True)
    atividade = models.TextField(max_length=255)
    dt_atividade = models.DateTimeField()
    #usuario_id = models.IntegerField()
    #id_especie = models.IntegerField()
