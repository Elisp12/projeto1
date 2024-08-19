from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from homespace.models import Categoria, Produto

@login_required
def lista_produto(request):

    lista_produtos = Produto.objects.all()

    context = {
        'lista_produtos': lista_produtos
    }
    return render(request, 'produto/lista_produto.html', context = context)