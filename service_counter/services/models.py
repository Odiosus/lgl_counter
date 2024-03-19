from django.db import models

from clients.models import Clients


class Services(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название услуги')
    description = models.CharField(max_length=255, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    services_status = models.BooleanField(default=True, verbose_name='Статус')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Услуги'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
