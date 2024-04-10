
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from empresa.views import EmpresaViewSet
from funcionario.views import FuncionarioViewSet
from funcionario.views import cadastrar_funcionario
from funcionario.views import fazer_login
from funcionario.views import editar_funcionario
from empresa.views import cadastrar_empresa
from produto.views import ProdutoViewSet

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
    path('editar/<int:funcionario_id>/', editar_funcionario, name='editar')
]
