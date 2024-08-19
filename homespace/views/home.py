from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from homespace.models import Categoria, Produto

@login_required
def home(request):

    lista_produtos = Produto.objects.all()

    context = {
        'lista_produtos': lista_produtos
    }
    return render(request, 'index.html', context = context)