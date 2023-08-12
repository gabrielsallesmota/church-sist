from django.urls import path
from apps.grupo_conexao.views import grupo_conexao_list, grupo_conexao_create, grupo_conexao_update, grupo_conexao_delete, generate_grupo_conexao_report

urlpatterns = [
    path('grupo_conexao_list/', grupo_conexao_list, name='grupo_conexao_list'),
    path('grupo_conexao_create/', grupo_conexao_create, name='grupo_conexao_create'),
    path('grupo_conexao_update/<int:pk>/', grupo_conexao_update, name='grupo_conexao_update'),
    path('grupo_conexao_delete/<int:pk>/', grupo_conexao_delete, name='grupo_conexao_delete'),
    path('reports_grupo_conexao/', generate_grupo_conexao_report, name='generate_grupo_conexao_report'),

]
