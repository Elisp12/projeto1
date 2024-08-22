from django.urls import path

from homespace.views.lista_produto import *
from homespace.views.lista_produtos_categoria import *
from homespace.views.produto_ativo import *
from homespace.views.produto_usuario import *


urlpatterns = [
    path('', lista_produto, name='lista_produto'),
    path('lista/produto/categoria/<int:index>/', lista_produto_categoria, name='lista_produto_categoria'),
    path('lista/produto/ativo/', produto_ativo, name='lista_produto_ativo'),
    path('usuario/produto/usuario/<int:id>/', produto_usuario, name = 'produto_usuario')
]