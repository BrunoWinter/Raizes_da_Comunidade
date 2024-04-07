from django.urls import path
from cad_usuario.views2 import cadastro

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro', )
]