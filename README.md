# RabbitMQ Email System

Um sistema simples de mensageria para envio de emails simulado, utilizando RabbitMQ, PostgreSQL e Flask. Esta aplicação demonstra como trabalhar com arquitetura baseada em filas, onde um serviço producer envia mensagens e um serviço consumer processa essas mensagens de forma assíncrona.

## Participante

Yasmin Victoria Oliveira RA: 812308

## Visão Geral

A aplicação simula um sistema de cadastro de usuários. Quando um novo usuário é cadastrado via API, uma mensagem com seus dados é enviada para uma fila RabbitMQ. O serviço consumer (worker) escuta essa fila e simula o envio de um email de boas-vindas para o usuário.

## Contêineres e Tecnologias Utilizadas

| Serviço    | Descrição                              | Tecnologia            |
|-------------|-----------------------------------------|-----------------------|
| `rabbitmq` | Gerenciador de filas (mensageria)       | RabbitMQ 3 Management |
| `postgres` | Banco de dados relacional               | PostgreSQL 14         |
| `producer` | API REST para cadastro de usuários      | Python, Flask, SQLAlchemy, pika |
| `consumer` | Worker que processa mensagens da fila   | Python, pika          |

Todos os serviços são orquestrados via Docker Compose.

---

## Manual de Instalação e Execução

### Pré-requisitos

- Ter o **Docker** e **Docker Compose** instalados.

### Clonando o projeto e subindo os containers

```bash
git clone https://github.com/seu-usuario/rabbitmq-email-system.git
cd rabbitmq-email-system
docker-compose up --build
```

### Acessos

Os seguintes serviços estarão ativos:

API Producer: http://localhost:5000

RabbitMQ UI: http://localhost:15672 (login: guest | senha: guest)

PostgreSQL: porta 5433

Consumer rodando em background, escutando a fila.

### Exemplos de uso

```bash
POST http://localhost:5000/register
Content-Type: application/json
{ nome: nome usuario
  email: email@email.com
}
# Exemplo de resposta:

{
  "message": "User nome usuario registered and queued for email."
}
