from datetime import timedelta

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычки"""

    PERIODICITY_CHOICES = {
        (1, 'каждый день'),
        (2, 'через день'),
        (3, 'каждый третий день'),
        (4, 'каждый четвертый день'),
        (5, 'каждый пятый день'),
        (6, 'каждый шестой день'),
        (7, 'каждую неделю')
    }

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              verbose_name='создатель',
                              **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=200, verbose_name='действие')
    is_enjoyable = models.BooleanField(verbose_name='приятная')
    linked_habit = models.ForeignKey('self',
                                     on_delete=models.SET_NULL,
                                     verbose_name='связанная приятная привычка',
                                     **NULLABLE)
    periodicity = models.IntegerField(choices=PERIODICITY_CHOICES,
                                      default=1,
                                      verbose_name='периодичность',
                                      **NULLABLE)
    treat = models.CharField(max_length=200,
                             verbose_name='вознаграждение',
                             **NULLABLE)
    duration = models.DurationField(verbose_name='время на выполнение',
                                    validators=[MaxValueValidator(timedelta(seconds=120))])
    is_public = models.BooleanField(verbose_name='публичная')

    def __str__(self):
        return f'Привычка {self.action} в {self.time} {self.periodicity}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
