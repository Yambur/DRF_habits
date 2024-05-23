from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.permissions import OwnerPermission
from habits.serializers import HabitSerializer
from habits.services import create_periodic_task, update_periodic_task, delete_periodic_task


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание новой привычки"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save(owner=self.request.user)
        create_periodic_task(habit)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [OwnerPermission]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирования одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [OwnerPermission]

    def perform_update(self, serializer):
        habit = serializer.save()
        update_periodic_task(habit)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаления одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, OwnerPermission]

    def perform_destroy(self, instance):
        delete_periodic_task(instance)
        return super().perform_destroy(instance)


class MyHabitListAPIView(generics.ListAPIView):
    """Вывод списка привычек пользователя"""
    serializer_class = HabitSerializer

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user).order_by('id')


class PublicHabitListAPIView(generics.ListAPIView):
    """Вывода списка публичных привычек"""
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True).order_by('id')