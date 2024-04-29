from django.urls import path
from app_cultivo.views import cultivo

urlpatterns = [
    path('cultivo/', cultivo, name='cultivo')
]
