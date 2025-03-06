from django.urls import path
from .views import chat_with_user

app_name = 'userchat'

urlpatterns = [
    path('<str:username>/', chat_with_user , name='chat_room'),
]
