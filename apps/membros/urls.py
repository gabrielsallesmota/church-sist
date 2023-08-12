from django.urls import path
from apps.membros.views import index, cadastro, consulta, editar, excluir, generate_membros_report,generate_aniversariantes_report

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('consulta/', consulta, name='consulta'),
    path('editar/<int:id>/', editar, name='editar'),
    path('excluir/<int:id>/', excluir, name='excluir'),
    path('reports/', generate_membros_report, name='reports'),
    path('reports_aniversario/', generate_aniversariantes_report, name='generate_aniversariantes_report'),
]