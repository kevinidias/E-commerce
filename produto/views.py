from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View


class ListaProdutos(ListView):
    pass


class DetalheProduto(View):
    pass


class AddCarrinho(View):
    pass


class DeleteCarrinho(View):
    pass


class Carrinho(View):
    pass


class Finalizar(View):
    pass