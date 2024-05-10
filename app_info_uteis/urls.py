from django.urls import path
from app_info_uteis.views import informacoes

urlpatterns = [
    path('info-uteis/', informacoes, name='info-uteis')
]