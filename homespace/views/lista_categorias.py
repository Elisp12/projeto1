from django.shortcuts import render

from homespace.models import Categoria

def lista_categoria(request):
    
    lista = Categoria.objects.all()

    context = {
        'lista_categoria' : lista,
    }

    return render(request, 'produto/lista_categoria.html', context = context)