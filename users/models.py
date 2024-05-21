from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    chat_id = models.CharField(max_length=50, verbose_name='ID чата в Telegram', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []