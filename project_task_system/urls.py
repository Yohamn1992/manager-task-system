# project_name/urls.py
from django.contrib import admin
from django.urls import path, include  # Importando 'include' para incluir URLs de aplicativos

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para a área administrativa do Django
    path('', include('tasks.urls')),  # Inclui as URLs do aplicativo 'tasks' para a raiz do site
]
