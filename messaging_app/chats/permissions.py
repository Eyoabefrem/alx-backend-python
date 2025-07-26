from rest_framework import permissions
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow users to access their own data.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only participants of a conversation
    to access or modify messages.
    """

    def has_permission(self, request, view):
        # Ensure user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is a participant in the conversation.
        `obj` here is a Message instance.
        """
        # Assuming `obj.conversation.participants` is a ManyToMany field
        return request.user in obj.conversation.participants.all()
