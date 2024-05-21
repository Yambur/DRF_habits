from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    MyHabitListAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete'),
    path('my-habits/', MyHabitListAPIView.as_view(), name='my-habits'),
    path('public/', PublicHabitListAPIView.as_view(), name='public'),
]