from rest_framework import serializers


class HabitTreatValidator:
    """
    Поля treat:
    Проверяет условия:
    1 - Заполняется одно поле, либо привычки, либо вознаграждения
    2 - Приятная привычка не вознаграждается
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        treat = value.get(self.field)
        linked_habit = value.get('linked_habit')
        is_enjoyable = value.get('is_enjoyable')
        if treat and is_enjoyable:
            raise serializers.ValidationError('Приятная привычка не вознаграждается')
        elif treat and linked_habit:
            raise serializers.ValidationError('Заполняется одно поле, либо привычки, либо вознаграждения')


class LinkedHabitValidator:
    """
    Поля связанной приятной привычки:
    Проверяет условия:
    1 - Приятная не может быть связана
    2 - Связанная привычка может быть только приятной
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        linked_habit = value.get(self.field)
        is_enjoyable = value.get('is_enjoyable')
        if linked_habit and is_enjoyable:
            raise serializers.ValidationError('Приятная не может быть связана')

        if linked_habit and not linked_habit.is_enjoyable:
            raise serializers.ValidationError('Связанная привычка может быть только приятной')
