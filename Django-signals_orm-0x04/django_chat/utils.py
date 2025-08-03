def get_threaded_messages(message):
    """
    Recursively fetches all replies to a message in threaded format.
    """
    result = []
    for reply in message.replies.all():
        result.append({
            "id": reply.id,
            "content": reply.content,
            "sender": reply.sender.username,
            "timestamp": reply.timestamp,
            "replies": get_threaded_messages(reply),
        })
    return result
