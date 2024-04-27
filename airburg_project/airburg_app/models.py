from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Название компании")
    country = models.CharField(max_length=30, blank=False, verbose_name="Страна компании")

    def __str__(self):
        return self.name


class Capitan(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Имя капитана")
    surname = models.CharField(max_length=30, blank=False, verbose_name="Фамилия капитана")
    experience = models.IntegerField(blank=False, verbose_name="Опыт пилотирования(в годах)")

    def __str__(self):
        return f"{self.name} {self.surname} Опыт полетов: {self.experience}"


class Airplane(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Название")
    count_pass = models.IntegerField( blank=False, verbose_name="Колличество пассажиров")
    wight = models.IntegerField(blank=False, verbose_name="Масса самолета в кг")
    fuel_reserve = models.IntegerField(blank=False, verbose_name="Запас топлива в км")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания")
    capitan = models.ForeignKey(Capitan, on_delete=models.CASCADE, verbose_name="Капитан")

    def __str__(self):
        return self.name
