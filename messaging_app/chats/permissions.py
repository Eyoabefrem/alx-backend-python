from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to authenticated users who are participants of the conversation.
    Applies to viewing, sending, updating, or deleting messages.
    """

    def has_permission(self, request, view):
        # Ensure user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is a participant in the conversation.
        Applies to all methods including PUT, PATCH, DELETE.
        """
        # Safe methods (GET, HEAD, OPTIONS) and unsafe (POST, PUT, PATCH, DELETE)
        allowed_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        if request.method in allowed_methods:
            return request.user in obj.conversation.participants.all()
        return False
