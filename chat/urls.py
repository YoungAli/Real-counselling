from django.urls import path
from . import views


urlpatterns = [
    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.view_message, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.get_send_message, name='message-detail'),
    path('api/messages/', views.get_send_message, name='message-list'),
]
