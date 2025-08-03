from django.contrib import admin
from .models import Message, Notification
from .models import Message, Notification, MessageHistory


admin.site.register(Message)
admin.site.register(Notification)

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'edited_at')
    search_fields = ('message__content',)
