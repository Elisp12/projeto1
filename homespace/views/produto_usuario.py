from django.contrib.auth.models import User
from django.shortcuts import render
from homespace.models import Produto

def produto_usuario(request, id):

    lista = Produto.objects.filter(athor = id).values('nome', 'descricao', 'quantidade', 'ativo', 'categoria', 'img', 'athor')
    
    context = {
        'produto_usuario': lista,
    }

    return render(request, 'usuario/produto_usuario.html', context = context)

