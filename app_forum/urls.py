from django.urls import path
from app_forum.views import forum, criar_topico, topico, criar_comentario

urlpatterns = [
    path('forum/', forum, name='forum'),
    path('forum/criar+topico', criar_topico, name='criar_topico'),
    path('forum/topico/<int:pk>', topico, name='topico'),
    path('forum/topico/<int:topico_id>/criar_comentario/', criar_comentario, name='criar_comentario'),
]