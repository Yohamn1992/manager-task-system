# tasks/urls.py
from django.urls import path
from . import views  # Importa as views do mesmo diretório

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL para a lista de tarefas
    path('new/', views.task_create, name='task_create'),  # URL para criar uma nova tarefa
    path('edit/<int:pk>/', views.task_update, name='task_update'),  # URL para editar uma tarefa existente
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),  # URL para excluir uma tarefa
]
