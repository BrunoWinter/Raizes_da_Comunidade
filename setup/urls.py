from django.contrib import admin
from django.urls import path
from app_cad_atividades import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home, name="home"),
    path("atividades/",views.atividades, name="atividade"),
    
]
