#!/usr/bin/env python3
"""
API views for chats app.

Implements ConversationViewSet and MessageViewSet using Django REST framework
viewsets to provide listing, creation, and retrieval endpoints.
"""

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """ViewSet for listing, retrieving, and creating conversations."""

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new conversation with participants.

        Expects a list of participant user IDs in the request data.
        """
        participants = request.data.get("participants", [])
        if not participants or not isinstance(participants, list):
            return Response(
                {"error": "Participants must be a non-empty list of user IDs."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        conversation = Conversation.objects.create()
        conversation.participants.set(participants)
        conversation.save()

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    """ViewSet for listing, retrieving, and creating messages."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        """
        Send a message in an existing conversation.

        Expects:
        - sender (user ID)
        - conversation (conversation ID)
        - message_body (text)
        """
        sender_id = request.data.get("sender")
        conversation_id = request.data.get("conversation")
        message_body = request.data.get("message_body")

        if not sender_id or not conversation_id or not message_body:
            return Response(
                {"error": "sender, conversation, and message_body are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate conversation exists
        try:
            conversation = Conversation.objects.get(pk=conversation_id)
        except Conversation.DoesNotExist:
            return Response(
                {"error": "Conversation does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        message = Message.objects.create(
            sender_id=sender_id, conversation=conversation, message_body=message_body
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
