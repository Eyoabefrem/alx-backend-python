from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessageSignalTestCase(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='alice', password='password123')
        self.receiver = User.objects.create_user(username='bob', password='password123')

    def test_notification_created_on_message_send(self):
        # Before sending message
        self.assertEqual(Notification.objects.count(), 0)

        # Create a message
        msg = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Hello, Bob!'
        )

        # After sending message
        self.assertEqual(Notification.objects.count(), 1)

        notification = Notification.objects.first()
        self.assertEqual(notification.user, self.receiver)
        self.assertEqual(notification.message, msg)
        self.assertFalse(notification.is_read)
