from conversation.models import Conversation


def messages_number(request):
    if request.user.is_authenticated:
        conversations = Conversation.objects.filter(members__in=[request.user.id], is_deleted=False)
        messages_number = 0
        for conversation in conversations:
            conversation_messages = conversation.messages.filter(is_read=False).exclude(created_by=request.user)
            conversation_messages_count = conversation_messages.count()
            messages_number += conversation_messages_count
    else:
        messages_number = 0

    return {'messages_number': messages_number}
