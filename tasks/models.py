from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]

    CATEGORY_CHOICES = [
        ('Trabalho', 'Trabalho'),
        ('Pessoal', 'Pessoal'),
        ('Outros', 'Outros'),
    ]

    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Progresso', 'Em Progresso'),
        ('Concluída', 'Concluída'),
        ('Arquivada', 'Arquivada'),
    ]

    title = models.CharField(max_length=200, help_text="Título da tarefa.")
    description = models.TextField(blank=True, help_text="Descrição detalhada da tarefa.")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Média', help_text="Prioridade da tarefa.")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Outros', help_text="Categoria da tarefa.")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pendente', help_text="Status da tarefa.")
    
    deadline = models.DateTimeField(help_text="Data limite para conclusão da tarefa.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Data de criação da tarefa.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Última vez que a tarefa foi atualizada.")

    completed = models.BooleanField(default=False, help_text="Indica se a tarefa foi concluída.")
    comments = models.TextField(blank=True, help_text="Comentários adicionais sobre a tarefa.")
    assigned_to = models.CharField(max_length=100, blank=True, help_text="Responsável pela tarefa.")
    estimated_time_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Tempo estimado para conclusão em horas.")

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        """Indica se a tarefa está atrasada"""
        return timezone.now() > self.deadline and not self.completed

    def clean(self):
        """Validações customizadas"""
        if self.deadline and self.deadline < timezone.now():
            raise ValidationError("A data limite não pode estar no passado.")
        if self.completed and self.status != 'Concluída':
            raise ValidationError("A tarefa está marcada como concluída, mas o status não reflete isso.")

    def save(self, *args, **kwargs):
        """Altera o status para 'Concluída' automaticamente ao marcar como 'completed'"""
        if self.completed:
            self.status = 'Concluída'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['deadline']
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
