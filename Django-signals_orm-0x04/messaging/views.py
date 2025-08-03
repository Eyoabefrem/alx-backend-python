from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    username = user.username
    user.delete()
    return Response({"message": f"User '{username}' deleted successfully."}, status=status.HTTP_200_OK)

@login_required
def unread_messages(request):
    user = request.user
    unread = Message.unread.for_user(user)
    data = [{"sender": m.sender.username, "content": m.content, "timestamp": m.timestamp} for m in unread]
    return JsonResponse(data, safe=False)
