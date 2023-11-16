
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import CreateClientViewset, ClientCreate

router = routers.DefaultRouter()
router.register(r'client', CreateClientViewset)

urlpatterns = [
    path('client_create/', ClientCreate.as_view(), name='client_create'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
