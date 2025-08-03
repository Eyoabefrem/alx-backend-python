# chats/views.py

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@method_decorator(cache_page(60), name='dispatch')
@method_decorator(login_required, name='dispatch')
class MessageListView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        messages = Message.objects.filter(receiver=user).order_by('-timestamp')
        return render(request, 'chats/message_list.html', {'messages': messages})

@cache_page(60)
@login_required
def conversation_messages(request):
    user = request.user
    messages = Message.objects.filter(receiver=user).order_by('-timestamp')
    return render(request, 'chats/message_list.html', {'messages': messages})
