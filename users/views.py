from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Регистрации пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Хеш пароля и сохранение пользователя"""
        user = serializer.save()
        user.set_password(user.password)
        user.save()
