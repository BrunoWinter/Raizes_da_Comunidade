from django.urls import path
from app_horta.views import criar_horta, minha_horta

urlpatterns = [
    path('horta/', minha_horta, name='minha_horta'),
    path('horta/criar', criar_horta, name='criar_horta')
]