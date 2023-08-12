from django.urls import path
from apps.eventos.views import evento_create, evento_delete, evento_list, evento_update, generate_eventos_report

urlpatterns = [
    path('evento_list/', evento_list, name='evento_list'),
    path('evento_create/', evento_create, name='evento_create'),
    path('evento_update/<int:pk>/', evento_update, name='evento_update'),
    path('evento_delete/<int:pk>/', evento_delete, name='evento_delete'),
    path('reports-eventos/', generate_eventos_report, name='generate_eventos_report'),
]
