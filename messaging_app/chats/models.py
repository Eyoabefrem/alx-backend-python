#!/usr/bin/env python3
"""
Django models for messaging_app chats app.

Defines:
- Custom User model extending AbstractUser with UUID primary key and extra fields.
- Conversation model tracking participants.
- Message model containing sender, conversation, and message content.
"""

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    """
    Custom User model extending AbstractUser.

    Fields:
    - user_id: UUID primary key, indexed.
    - first_name: inherited, required.
    - last_name: inherited, required.
    - email: unique, required.
    - password: inherited (hashed password).
    - phone_number: optional.
    - role: ENUM('guest', 'host', 'admin'), required.
    - created_at: timestamp, default to current time.
    """

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    # first_name and last_name inherited, but mark non-null with blank=False
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.email} ({self.role})"


class Conversation(models.Model):
    """
    Conversation model representing a chat between multiple users.

    Fields:
    - conversation_id: UUID primary key, indexed.
    - participants: many-to-many relation with User.
    - created_at: timestamp, default to current time.
    """

    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Conversation {self.conversation_id}"


class Message(models.Model):
    """
    Message model containing message content within a conversation.

    Fields:
    - message_id: UUID primary key, indexed.
    - sender: ForeignKey to User.
    - conversation: ForeignKey to Conversation.
    - message_body: text content.
    - sent_at: timestamp, default to current time.
    """

    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField(blank=False)
    sent_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message {self.message_id} from {self.sender.email}"
