
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import CreateClientViewset, Chat_bot_edit_client

router = routers.DefaultRouter()
router.register(r'client', CreateClientViewset)
router.register(r'chat_bot', Chat_bot_edit_client, basename='chat_bot')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]