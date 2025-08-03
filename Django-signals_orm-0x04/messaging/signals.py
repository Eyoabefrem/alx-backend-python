from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification
from django.db.models.signals import pre_save
from .models import Message, MessageHistory
from django.db.models.signals import post_delete
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def create_notification_on_new_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )

@receiver(pre_save, sender=Message)
def log_message_edits(sender, instance, **kwargs):
    if not instance.pk:
        return  # Message is new, not edited

    try:
        original = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return

    if original.content != instance.content:
        # Save the old content in MessageHistory
        MessageHistory.objects.create(
            message=original,
            old_content=original.content
        )
        instance.edited = True

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Deletes all messages where user is sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Deletes all notifications associated with user
    Notification.objects.filter(user=instance).delete()

    # Deletes message histories for user messages
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()
