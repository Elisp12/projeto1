from django.urls import path
from homespace.views.lista_produto import *

urlpatterns = [
    path('', lista_produto, name='home')
]