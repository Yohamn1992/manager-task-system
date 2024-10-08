from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm  # Não esqueça de importar o TaskForm
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# View para o login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Template de login
    success_url = reverse_lazy('task_list')  # Redireciona para a lista de tarefas após o login

# View para listar as tarefas
@login_required  # Garante que o usuário esteja logado para acessar a lista de tarefas
def task_list(request):
    tasks = Task.objects.all()  # Busca todas as tarefas
    overdue_tasks = tasks.filter(deadline__lt=timezone.now(), completed=False)  # Tarefas atrasadas
    user = request.user  # Obtém o usuário logado
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'overdue_tasks': overdue_tasks, 'user': user})

# View para criar uma nova tarefa
@login_required  # Garante que o usuário esteja logado
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redireciona para a lista de tarefas após salvar
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# View para atualizar uma tarefa existente
@login_required  # Garante que o usuário esteja logado
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redireciona para a lista de tarefas após salvar
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# View para deletar uma tarefa
@login_required  # Garante que o usuário esteja logado
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redireciona para a lista de tarefas após excluir
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})  # Renderiza a página de confirmação

# View para o registro de usuários
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o cadastro
            return redirect('task_list')  # Redireciona para a página de lista de tarefas
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# View para editar os dados de perfil do usuário
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redireciona para a lista de tarefas após salvar
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'tasks/edit_profile.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html', {})
