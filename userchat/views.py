from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def chat_with_user(request, username):
    user_to_chat = get_object_or_404(User, username=username)
    return render(request, 'chat.html', {'user_to_chat': user_to_chat})
