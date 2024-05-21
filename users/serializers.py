from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя"""
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'chat_id')
        extra_kwargs = {'password': {'write_only': True}}