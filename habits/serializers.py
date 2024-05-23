from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitTreatValidator, LinkedHabitValidator, duration_validator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализотор привычки"""
    duration = serializers.DurationField(validators=[duration_validator])

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['owner']
        validators = [
            HabitTreatValidator(field='treat'),
            LinkedHabitValidator(field='linked_habit')
        ]