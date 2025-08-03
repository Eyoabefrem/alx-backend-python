from django.urls import path
from .views import delete_user
from . import views

urlpatterns = [
    path('delete-account/', delete_user, name='delete_account'),
    path('inbox/unread/', views.unread_messages, name='unread_messages'),
]
