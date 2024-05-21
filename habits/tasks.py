from celery import shared_task

from habits.services import remind_of_habit


@shared_task
def habit_reminder(habit_id):
    """
    Таск Celer, напоминания о привычки
    :param habit_id: id привычки (Habit)
    """
    remind_of_habit(habit_id)
