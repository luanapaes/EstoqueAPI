
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from empresa.views import EmpresaViewSet
from funcionario.views import FuncionarioViewSet
from funcionario.views import cadastrar_funcionario
from funcionario.views import fazer_login
from funcionario.views import editar_funcionario
from funcionario.views import excluir_funcionario
from empresa.views import cadastrar_empresa
from produto.views import ProdutoViewSet, cadastrar_produto, editar_produto, excluir_produto

router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('cadastrar-funcionario/', cadastrar_funcionario,
         name='cadastrar_funcionario'),
    path('cadastrar-empresa/', cadastrar_empresa, name='cadastrar-empresa'),
    path('login/', fazer_login, name='login'),
    path('editar-funcionario/<int:funcionario_id>/', editar_funcionario, name='editar-funcionario'),
    path('excluir-funcionario/<int:funcionario_id>/', excluir_funcionario, name='excluir-funcionario'),
    path('cadastrar-produto/', cadastrar_produto, name='cadastrar-produto'),
    path('editar-produto/<int:produto_id>/', editar_produto, name='editar-produto'),
    path('excluir-produto/<int:produto_id>/',
         excluir_produto, name='excluir-produto')
]
