from django.urls import path
from app_cad_usuario.views2 import cadastro, user_login

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', user_login, name='login')
]