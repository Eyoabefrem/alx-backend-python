#!/usr/bin/env python3
"""
Views for handling API requests related to Conversations and Messages.
"""

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter
from .pagination import MessagePagination
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN


class ConversationViewSet(viewsets.ModelViewSet):
    """ViewSet for listing, creating, and retrieving conversations."""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__first_name', 'participants__last_name']


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for listing, creating, and retrieving messages in a conversation."""
    serializer_class = MessageSerializer

    def get_queryset(self):
        """Return messages for a specific conversation."""
        conversation_id = self.kwargs['conversation_pk']
        return Message.objects.filter(conversation_id=conversation_id)

    def create(self, request, *args, **kwargs):
        """Create a new message in a conversation."""
        conversation_id = self.kwargs['conversation_pk']
        data = request.data.copy()
        data['conversation'] = conversation_id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageViewSet(viewsets.ModelViewSet):
    ...
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        # Filter messages to only those the user is allowed to see
        return Message.objects.filter(conversation__participants=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter
    pagination_class = MessagePagination

    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)

def perform_create(self, serializer):
    conversation = serializer.validated_data['conversation']
    user = self.request.user

    if user not in conversation.participants.all():
        return Response({"detail": "You are not a participant of this conversation."}, status=HTTP_403_FORBIDDEN)

    serializer.save(sender=user)

def get_queryset(self):
    queryset = Message.objects.filter(conversation__participants=self.request.user)

    if not self.request.user.is_authenticated:
        return Response({"detail": "Not authenticated."}, status=HTTP_403_FORBIDDEN)

    return queryset
