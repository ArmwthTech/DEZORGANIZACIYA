from .models import Client
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
class ClientSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(region="RU")

    class Meta:
        model = Client
        fields = ['id', 'last_name', 'first_name', 'patronymic',
                  'age', 'email', 'current_profession', 'work_experience', 'salary',
                  'phone',]

