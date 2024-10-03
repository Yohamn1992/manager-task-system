from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm  # Não esqueça de importar o TaskForm
from django.utils import timezone

def task_list(request):
    tasks = Task.objects.all()  # Busca todas as tarefas
    overdue_tasks = tasks.filter(deadline__lt=timezone.now(), completed=False)  # Tarefas atrasadas
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'overdue_tasks': overdue_tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redireciona para a lista de tarefas após salvar
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

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

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redireciona para a lista de tarefas após excluir
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})  # Renderiza a página de confirmação
