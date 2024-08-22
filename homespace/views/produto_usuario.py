from django.contrib.auth.models import User
from django.shortcuts import render
from homespace.models import Produto

def produto_usuario(request, id):

    lista = Produto.objects.filter(athor = id).values('nome', 'descricao', 'quantidade', 'ativo', 'categoria', 'img', 'athor')

    usuario = User.objects.filter(id = id).values('username')
    
    context = {
        'produto_usuario': lista,
        'usuario': usuario,
    }

    return render(request, 'usuario/produto_usuario.html', context = context)

