from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProduto.as_view(), name="detalhe"),
    path('addcarrinho/', views.AddCarrinho.as_view(), name="addcarrinho"),
    path('deletecarrinho/', views.DeleteCarrinho.as_view(), name="deletecarrinho"),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho"),
    path('finalizar/', views.Finalizar.as_view(), name="finalizar"),
]
