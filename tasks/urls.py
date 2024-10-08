from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView  # Importando a view de logout

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),  # Página de login como página inicial
    path('register/', views.register, name='register'),  # Página de cadastro
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/update/<int:pk>/', views.task_update, name='task_update'),
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # Rota para editar perfil
    path('logout/', LogoutView.as_view(), name='logout'),  # Rota para logout
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
