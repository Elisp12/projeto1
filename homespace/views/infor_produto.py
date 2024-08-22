from django.shortcuts import render

from homespace.models import Produto

def infor_produto(request, index):
    infor = Produto.objects.filter(index = index).all()

    print(infor)

    context = {
        'infor_produto': infor,
    }

    return render(request, 'produto/infor_produto.html', context = context)