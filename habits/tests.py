from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тест бля модели привычки"""

    def setUp(self):
        self.user = User.objects.create(email='test@test.ru')
        self.user2 = User.objects.create(email='test2@test.ru')
        self.habit = Habit.objects.create(action='Test action',
                                          place='Test place',
                                          time='19:00',
                                          is_enjoyable=False,
                                          treat='Test treat',
                                          is_public=True,
                                          duration=timedelta(minutes=1),
                                          owner=self.user)
        self.enjoyable_habit = Habit.objects.create(action='Test enjoyable action',
                                                    place='Test enjoyable place',
                                                    time='19:00',
                                                    is_enjoyable=True,
                                                    is_public=True,
                                                    duration=timedelta(minutes=1),
                                                    owner=self.user)

    def test_habit_list_public(self):
        """Тест вывода списка публичных привычек"""
        url = reverse('habits:public')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list_for_owner(self):
        """Тест вывода списка привычек пользователя"""
        url = reverse('habits:my-habits')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }
                         )

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data.get('results')), 2)

    def test_habit_retrieve(self):
        """Тест вывода одной привычки пользователя"""
        url = reverse('habits:retrieve', args=(self.habit.pk,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('id'), self.habit.pk)

    def test_habit_update(self):
        """Тест обновления привычки"""
        url = reverse('habits:update', args=(self.habit.pk,))
        data = {'action': 'Updated test action'}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('action'), 'Updated test action')

    def test_habit_delete(self):
        """Тест удаления привычки"""
        url = reverse('habits:delete', args=(self.habit.pk,))

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 1)
