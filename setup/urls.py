from django.contrib import admin
from django.urls import path, include
from app_cad_atividades import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home, name="home"),
    path("atividades/",views.atividades, name="atividade"),
    path('cadastro/', include('app_cad_usuario.urls')),
    path('login/', include('app_cad_usuario.urls')),
    path('authuser/', include('app_horta.urls')),
    path('cultivo/', include('app_cultivo.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
