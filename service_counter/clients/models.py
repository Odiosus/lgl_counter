from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    brand_name = models.CharField(max_length=100, verbose_name='Фирменное наименование')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    ogrn = models.CharField(max_length=13, verbose_name='ОГРН')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    agent = models.ForeignKey('ClientAgent', on_delete=models.PROTECT, null=True, verbose_name='Представитель')
    agreement = models.ForeignKey('Agreement', on_delete=models.PROTECT, null=True, verbose_name='Договор')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class ClientAgent(models.Model):
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Представитель'
        verbose_name_plural = 'Представители'

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}'


class Agreement(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование договора')
    number = models.CharField(max_length=100, verbose_name='Номер договора')
    date = models.DateField(verbose_name='Дата договора')
    description = models.CharField(max_length=255, verbose_name='Описание')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, verbose_name='Клиент')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    def __str__(self):
        return self.name