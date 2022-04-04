from django.db import models


class Pacient(models.Model):
    """
    Пациенты
    """
    name = models.CharField(max_length=30, verbose_name='Имя')
    second_name = models.CharField(max_length=50, verbose_name='Фамилия')
    last_name = models.CharField(max_length=50, verbose_name='Отчество')
    date_b = models.DateField(blank=False, verbose_name='Дата рождения')
