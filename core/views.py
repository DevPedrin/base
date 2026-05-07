from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm


# LISTAR
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista.html', {'produtos': produtos})


# CRIAR
def criar_produto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'form.html', {'form': form})


# EDITAR
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'form.html', {'form': form})


# DELETAR
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    produto.delete()

    return redirect('lista_produtos')