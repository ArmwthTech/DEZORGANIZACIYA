from django import forms
from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'patronymic',
                  'age', 'email', 'current_profession', 'work_experience', 'salary',
                  'phone',]