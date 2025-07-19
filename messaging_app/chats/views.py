#!/usr/bin/env python3
"""
Views for handling API requests related to Conversations and Messages.
"""

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


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
