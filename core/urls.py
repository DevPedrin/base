from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),

    path('criar/', views.criar_produto, name='criar_produto'),

    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),

    path('deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
]