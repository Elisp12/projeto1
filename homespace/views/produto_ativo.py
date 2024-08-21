from django.shortcuts import render 

from homespace.models import Produto

# def produto_ativo(request, index):
#     ativo = Produto.objects.filter(ativo = index).all()

#     context = {
#         'produto_ativo': ativo,
#     }

#     return render(request, 'produto/produto_ativo.html', context = context)

def produto_ativo(request):

    ativado =Produto.objects.filter(ativo = True).values('nome', 'descricao', 'quantidade', 'ativo', 'categoria', 'img', 'athor')

    context = {
        'produto_ativo': ativado,
    }

    return render(request, 'produto/produto_ativo.html', context =context)