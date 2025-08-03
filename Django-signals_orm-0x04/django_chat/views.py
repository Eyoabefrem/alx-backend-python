from .models import Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def user_conversation_view(request):
    messages = Message.objects.filter(receiver=request.user, parent_message=None) \
                .select_related('sender', 'receiver') \
                .prefetch_related('replies__sender', 'replies__receiver')

    context = {
        "messages": messages,
    }
    return render(request, "chat/conversation.html", context)
