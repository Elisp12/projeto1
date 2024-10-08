from django.urls import path

from homespace.views.lista_produto import *
from homespace.views.lista_produtos_categoria import *
from homespace.views.produto_ativo import *
from homespace.views.produto_usuario import *
from homespace.views.infor_produto import *
from homespace.views.lista_categorias import *


urlpatterns = [
    path('', lista_produto, name='lista_produto'),
    path('lista/produto/categoria/<int:index>/', lista_produto_categoria, name='lista_produto_categoria'),
    path('lista/produto/ativo/', produto_ativo, name='lista_produto_ativo'),
    path('usuario/produto/usuario/<int:id>/', produto_usuario, name = 'produto_usuario'),
    path('infor/produto/<int:index>/', infor_produto, name='infor_produto'),
    path('lista/categoria/', lista_categoria, name='lista_categoria'),
]