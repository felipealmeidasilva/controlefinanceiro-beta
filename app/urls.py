from django.urls import path
from .views import home, contato, adicionar_cadastro, listar_cadastro, modificar_cadastro, eliminar_cadastro

urlpatterns = [
    path('', home, name="home"),
    path('contato/', contato, name="contato"),
    path('adicionar-cadastro/', adicionar_cadastro, name="adicionar_cadastro"),
    path('listar-cadastro/', listar_cadastro, name="listar_cadastro"),
    path('modificar-cadastro/<id>/', modificar_cadastro, name="modificar_cadastro"),
    path('eliminar-cadastro/<id>/', eliminar_cadastro, name="eliminar_cadastro"),
]