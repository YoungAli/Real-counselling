from users.models import CustomUser
from rest_framework import serializers
from chat.models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=CustomUser.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=CustomUser.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
