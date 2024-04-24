from django.urls import path
from app_forum.views import forum

urlpatterns = [
    path('forum/', forum, name='forum'),
]