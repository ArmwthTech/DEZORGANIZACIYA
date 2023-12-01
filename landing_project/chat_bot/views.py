from django.shortcuts import render
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
from rest_framework.decorators import api_view, renderer_classes, schema
from ast import literal_eval
from rest_framework.schemas.openapi import AutoSchema
# Create your views here.

class CreateClientViewset(ViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['post', 'get']
    renderer_classes = [JSONRenderer]
    def list(self, request):
        client = Client.objects.create(full_name='process')
        client_back = ClientSerializer(client)
        id = {'id':client_back.data['id']}
        client.delete()
        return Response(data=id)
    def create(self, request):
        #print(request.data)
        if request.data['status'] == 'end':
            data = chat_bot_client(request.data['id'])
            client = ClientForm(data)
        else:
            client = ClientForm(request.data)

        print(client.is_valid())
        if client.is_valid():
            client.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Chat_bot_edit_client(ViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['post']
    renderer_classes = [JSONRenderer]

    def create(self, request):
        bd_file = open('bd.txt', 'r+', encoding='utf-8')
        data = request.data
        id_ = data['id']

        for line in bd_file:
            if line == '\n':
                break
            dict_ = literal_eval(line)  # ast
            if dict_['id'] == id_:
                bd_file.close()

                bd_file = open('bd.txt', 'rt', encoding='utf-8')
                text = bd_file.read()
                dict_.update(data)
                text = text.replace(line, str(dict_) + '\n')
                bd_file.close()

                bd_file = open('bd.txt', 'wt', encoding='utf-8')
                bd_file.write(text)
                bd_file.close()
                return Response(status=status.HTTP_202_ACCEPTED)

        bd_file.seek(0, 2)
        bd_file.write(str(data)+'\n')
        bd_file.close()

        return Response(status=status.HTTP_201_CREATED)


def chat_bot_client(id_):
    bd_file = open('bd.txt', 'r', encoding='utf-8')

    for line in bd_file:
        if line == '\n':
            return {}
        dict_ = literal_eval(line)
        if dict_['id'] == id_:
            return dict_