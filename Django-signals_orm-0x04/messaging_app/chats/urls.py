from django.urls import path
from .views import conversation_messages  # or MessageListView

urlpatterns = [
    path('conversations/', conversation_messages, name='conversation_messages'),
    # OR if using the class-based view:
    # path('conversations/', MessageListView.as_view(), name='conversation_messages'),
]
