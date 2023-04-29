from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item
from .models import Conversation, ConversationMessage
from .forms import ConversationMessageForm


# Create your views here.
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass  # redirect to conversation

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form,
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id], is_deleted=False)
    conversations_number_all = conversations.count()

    messages = ConversationMessage.objects.filter(is_delivered=False)
    messages_r = messages.exclude(created_by=request.user)

    for message_r in messages_r:
        message_r.mark_as_delivered()

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
        'conversations_number_all': conversations_number_all,
    })


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    messages = conversation.messages.all()

    new_messages = conversation.messages.filter(is_read=False).exclude(created_by=request.user)
    for new_message in new_messages:
        new_message.mark_as_read()

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()
            return redirect('conversation:detail', pk=pk)

    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'messages': messages,
        'form': form,
    })


def delete_conversation(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    conversation.is_deleted=True
    conversation.save()

    return redirect('conversation:inbox')






















