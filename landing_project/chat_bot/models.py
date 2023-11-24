from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Client(models.Model):
    age = models.IntegerField(blank=True)
    full_name = models.CharField(blank=True, max_length=128)
    email = models.EmailField()
    date_create = models.DateTimeField(auto_now_add=True)
    current_profession = models.CharField(max_length=128, blank=True)
    #Пока поставил int, надо будет обсудить тип данных для стажа работы
    work_experience = models.IntegerField(blank=True)
    salary = models.IntegerField(blank=True)
    #https://django-phonenumber-field.readthedocs.io/en/latest/index.html
    phone = PhoneNumberField(blank=False, region='RU')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'