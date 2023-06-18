from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from users.models import CustomUser
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message
from chat.serializers import MessageSerializer
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@csrf_exempt
def get_send_message(request, sender=None, receiver=None):
    """
    gets all messages, and create a new message
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@login_required(login_url='login')
def chat_view(request):
    if request.method == "GET":
        unread_chats_count, unread_chats = 0, {}
        for user in CustomUser.objects.all():
            chats = Message.objects.filter(sender=user, is_read=False).count()
            unread_chats_count += chats
            unread_chats.update({user.first_name: chats})

        return render(request, 'chat.html', {"users": CustomUser.objects.exclude(first_name=request.user.first_name), "unread_chats":unread_chats})

@login_required(login_url='login')
def view_message(request, sender, receiver):
    if request.method == "GET":
        unread_chats_count, unread_chats = 0, {}
        for user in CustomUser.objects.all():
            chats = Message.objects.filter(sender=user, is_read=False).count()
            unread_chats_count += chats
            unread_chats.update({user.first_name: chats})
        print('=====', unread_chats_count)


        return render(request, "messages.html",
            {
                'users': CustomUser.objects.exclude(first_name=request.user.first_name),
                'receiver': CustomUser.objects.get(id=receiver),
                'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) | Message.objects.filter(sender_id=receiver, receiver_id=sender),
                'unread_chats': unread_chats
            }
        )
