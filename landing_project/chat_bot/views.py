from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ClientForm
from rest_framework.viewsets import ViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from phonenumber_field.phonenumber import PhoneNumber
from rest_framework.renderers import JSONRenderer
# Create your views here.

class CreateClientViewset(ViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['post',]

    def create(self, request):
        print(request.data)
        try:
            PhoneNumber.from_string(request.data['phone'], region='RU')
        except:
            data = {'status': 400, 'text': 'Неправильный номер', }
            return JSONRenderer().render(data)
        client = ClientForm(request.data)


        if client.is_valid():
            client.save()
            data = {'status': 201, }
            return JSONRenderer().render(data)
        else:
            data = {'status': 400, }
            return JSONRenderer().render(data)

class ClientCreate(CreateView):
    form_class = ClientForm
    model = Client
    success_url = 'client_create'
    template_name = 'client_create.html'
