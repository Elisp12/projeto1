from django.shortcuts import render

from homespace.models import Categoria, Produto

def lista_produto_categoria(request, index):
    
    lista = Produto.objects.filter(categoria = index).all()

    context = {
        'lista_produto_categoria': lista,
    }
    return render(request, 'produto/lista_produto_categoria.html', context = context)