#!/usr/bin/env python3
"""
Serializers for User, Conversation, and Message models with validations.
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Conversation, Message


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'role']


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for the Message model."""

    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model."""

    participants = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at', 'messages']

    def get_messages(self, obj):
        """Get messages related to the conversation."""
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data

    def validate_participants(self, value):
        """Ensure there are at least two participants."""
        if len(value) < 2:
            raise serializers.ValidationError("A conversation must have at least two participants.")
        return value
