from django.urls import path
from app_forum.views import forum, criar_topico

urlpatterns = [
    path('forum/', forum, name='forum'),
    path('forum/criar+topico', criar_topico, name='criar_topico')
]