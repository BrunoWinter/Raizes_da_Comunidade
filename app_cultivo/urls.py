from django.urls import path
from app_cultivo.views import cultivo, pesquisa

urlpatterns = [
    path('cultivo/', cultivo, name='cultivo'),
    path('cultivo/pesquisa/', pesquisa, name='pesquisa')
]
