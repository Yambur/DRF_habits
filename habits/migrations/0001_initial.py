# Generated by Django 4.2 on 2024-05-21 19:34

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=200, verbose_name='действие')),
                ('is_enjoyable', models.BooleanField(verbose_name='приятная')),
                ('periodicity', models.IntegerField(blank=True, choices=[(3, 'каждый третий день'), (7, 'каждую неделю'), (5, 'каждый пятый день'), (6, 'каждый шестой день'), (4, 'каждый четвертый день'), (1, 'каждый день'), (2, 'через день')], default=1, null=True, verbose_name='периодичность')),
                ('treat', models.CharField(blank=True, max_length=200, null=True, verbose_name='вознаграждение')),
                ('duration', models.DurationField(validators=[django.core.validators.MaxValueValidator(datetime.timedelta(seconds=120))], verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(verbose_name='публичная')),
                ('linked_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная приятная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]