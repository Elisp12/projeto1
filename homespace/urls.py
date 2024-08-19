from django.urls import path

from homespace.views.lista_produto import *
from homespace.views.lista_produtos_categoria import *
from homespace.views.produto_ativo import *


urlpatterns = [
    path('', lista_produto, name='lista_produto'),
    path('lista/produto/categoria/<int:index>/', lista_produto_categoria, name='lista_produto_categoria'),
    path('lista/produto/ativo/<int:index>/', produto_ativo, name='lista_produto_ativo'),
]