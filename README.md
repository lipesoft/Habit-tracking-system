## Habit Tracking System

Um sistema de gerenciamento de hábitos via linha de comando (CLI) focado em persistência de dados e lógica relacional.

## Sobre o Projeto
Este projeto foi desenvolvido para demonstrar competências essenciais de um desenvolvedor backend: manipulação de bancos de dados SQL, lógica de negócios em Python e organização de código modular.

O sistema permite criar usuários, gerenciar hábitos específicos para cada usuário e registrar o progresso diário com logs detalhados.

## Stack Técnica
- **Linguagem:** Python 3.x
- **Banco de Dados:** SQLite3 (Relacional)
- **Interface:** Terminal (CLI)

## Arquitetura do Banco de Dados
O banco foi modelado seguindo as boas práticas de normalização:
- `users`: Armazena dados de perfil.
- `habits`: Relaciona hábitos a um `user_id` (FK).
- `habit_logs`: Registra o histórico diário de cada hábito.

## Funcionalidades (CRUD)
- Cadastro e listagem de usuários.
- Criação de hábitos vinculados a usuários.
- Registro de progresso com validação de status.
- Consulta de histórico de progresso ordenado por data.
