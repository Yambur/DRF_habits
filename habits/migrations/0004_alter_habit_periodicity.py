# Generated by Django 4.2 on 2024-05-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.IntegerField(blank=True, choices=[(7, 'каждую неделю'), (6, 'каждый шестой день'), (1, 'каждый день'), (4, 'каждый четвертый день'), (3, 'каждый третий день'), (2, 'через день'), (5, 'каждый пятый день')], default=1, null=True, verbose_name='периодичность'),
        ),
    ]
