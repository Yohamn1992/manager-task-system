# Manager Task System

Este projeto é um sistema de gerenciamento de tarefas desenvolvido em Django, que permite criar, editar e gerenciar tarefas com diferentes níveis de prioridade, categorias e status. Ele também fornece funcionalidades como validação de data de conclusão e controle de atrasos.

## Funcionalidades Principais

- **Criação de Tarefas**: Permite adicionar tarefas com um título, descrição, prioridade, categoria, status, data limite, responsável, tempo estimado e comentários adicionais.
- **Atualização de Tarefas**: Atualize o status, prioridade e outros detalhes da tarefa conforme o progresso.
- **Marcação de Conclusão**: Ao marcar uma tarefa como concluída, o sistema automaticamente atualiza seu status.
- **Controle de Atrasos**: O sistema verifica se uma tarefa está atrasada com base na data limite e na conclusão.
- **Validações Customizadas**: Validações automáticas impedem que uma data limite no passado seja definida e verificam a consistência entre o campo de conclusão e o status.

## Modelos

### Task (Tarefa)

Este é o modelo principal do sistema. Ele representa uma tarefa que possui os seguintes campos:

- **Título (`title`)**: Um campo de texto (máx. 200 caracteres) que define o título da tarefa.
- **Descrição (`description`)**: Um campo de texto opcional para detalhar a tarefa.
- **Prioridade (`priority`)**: Um campo de escolha com três opções: `Baixa`, `Média` (padrão) e `Alta`. Define a importância da tarefa.
- **Categoria (`category`)**: Um campo de escolha com três opções: `Trabalho`, `Pessoal`, `Outros` (padrão). Organiza as tarefas em categorias.
- **Status (`status`)**: Um campo de escolha que define o estado atual da tarefa. Opções: `Pendente` (padrão), `Em Progresso`, `Concluída` e `Arquivada`.
- **Data Limite (`deadline`)**: Um campo de data e hora que indica o prazo para a conclusão da tarefa. Este campo não pode ser no passado.
- **Data de Criação (`created_at`)**: Data de criação da tarefa (auto preenchido pelo sistema).
- **Última Atualização (`updated_at`)**: Data da última atualização da tarefa (auto preenchido pelo sistema).
- **Concluída (`completed`)**: Um campo booleano que indica se a tarefa foi marcada como concluída.
- **Comentários (`comments`)**: Um campo opcional para adicionar comentários ou observações sobre a tarefa.
- **Responsável (`assigned_to`)**: Um campo opcional que define quem é o responsável pela tarefa.
- **Tempo Estimado (`estimated_time_hours`)**: Um campo numérico opcional para indicar o tempo estimado para conclusão da tarefa (em horas).

### Propriedades e Métodos

- **`is_past_due`**: Um método que retorna `True` se a tarefa estiver atrasada (data limite ultrapassada e tarefa não concluída).
- **Validações Customizadas**: 
  - A data limite não pode estar no passado.
  - Se a tarefa está marcada como `concluída`, o status deve ser "Concluída".
- **Método `save()`**: Atualiza automaticamente o status para "Concluída" ao marcar a tarefa como concluída.

## Validações Customizadas

O modelo `Task` inclui validações que garantem a consistência dos dados:
- A data limite (`deadline`) não pode ser uma data anterior à data atual.
- Se a tarefa for marcada como `concluída`, o status deve ser ajustado para "Concluída".

## Ordenação de Tarefas

As tarefas são ordenadas automaticamente pela data limite (`deadline`), o que facilita a priorização de tarefas mais urgentes.

## Tecnologias Utilizadas

- **Python 3.8+**
- **Django**
- **SQLite** (pode ser substituído por outro banco de dados, como PostgreSQL)
- **Git** (para controle de versão)
- **GitHub** (para repositório remoto)

## Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/Yohamn1992/manager-task-system.git
