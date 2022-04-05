from django.db import models


class Pacient(models.Model):
    """
    Пациенты
    """
    name = models.CharField(max_length=30, verbose_name='Имя')
    second_name = models.CharField(max_length=50, verbose_name='Фамилия')
    last_name = models.CharField(max_length=50, verbose_name='Отчество')
    date_b = models.DateField(blank=False, verbose_name='Дата рождения')


class Special(models.Model):

    name = models.CharField(max_length=200, verbose_name='Название')

    def str(self):
        return self.name


class Skill(models.Model):

    name = models.CharField(max_length=200, verbose_name='Название')
    koef = models.FloatField(verbose_name='Коэффициент')

    def str(self):
        return self.name


class Employes(models.Model):

    name = models.CharField(max_length=30, verbose_name='Имя')
    second_name = models.CharField(max_length=50, verbose_name='Фамилия')
    last_name = models.CharField(max_length=50, verbose_name='Отчество')
    special = models.ForeignKey(Special, on_delete=models.DO_NOTHING, verbose_name='Специальность')
    skill = models.ForeignKey(Skill, on_delete=models.DO_NOTHING, verbose_name='Квалификация')

class Diagnosis(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название')
    cost = models.IntegerField(verbose_name='Стоимость лечения')