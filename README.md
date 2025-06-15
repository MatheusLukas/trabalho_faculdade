# Sistema de Gestão Escolar

Este é um sistema de gestão escolar desenvolvido para a UniFAAT, utilizando microserviços em Python e PostgreSQL como banco de dados.

## 🚀 Tecnologias Utilizadas

- Python (Backend)
- PostgreSQL (Banco de Dados)
- Docker & Docker Compose
- Prometheus (Monitoramento)
- Grafana (Visualização de Métricas)
- Flask (Framework Web)
- Flasgger (Documentação da API)

## 📋 Pré-requisitos

- Docker
- Docker Compose
- Git

## 🔧 Instalação e Execução

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Execute o ambiente com Docker Compose:
```bash
docker-compose up -d
```

## 🌐 Acesso aos Serviços

Após a inicialização, os seguintes serviços estarão disponíveis:

- Backend API: http://localhost:5000
- Documentação da API (Swagger): http://localhost:5000/apidocs
- Banco de Dados PostgreSQL: localhost:3001
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090

## 📊 Estrutura do Banco de Dados

O sistema utiliza um banco de dados PostgreSQL com as seguintes tabelas principais:

- `professor`: Cadastro de professores
- `turma`: Gerenciamento de turmas
- `aluno`: Cadastro de alunos
- `pagamento`: Controle de pagamentos
- `presenca`: Registro de presenças
- `atividade`: Atividades escolares
- `atividade_aluno`: Relacionamento entre atividades e alunos
- `usuario`: Sistema de autenticação

### Detalhes das Tabelas

#### Professor
- id_professor (PK)
- nome_completo
- email
- telefone

#### Turma
- id_turma (PK)
- nome_turma
- id_professor (FK)
- horario

#### Aluno
- id_aluno (PK)
- nome_completo
- data_nascimento
- id_turma (FK)
- nome_responsavel
- telefone_responsavel
- email_responsavel
- endereco
- cidade
- estado
- cep
- pais
- telefone

## 🔍 Monitoramento

O sistema inclui monitoramento através do Prometheus e Grafana:

- Prometheus: Coleta métricas do sistema
- Grafana: Visualização de métricas e dashboards
- Postgres Exporter: Métricas específicas do PostgreSQL

## 📁 Estrutura do Projeto

```
.
├── InfraBD/              # Configurações do Banco de Dados
│   ├── northwind.sql     # Script SQL
│   └── dockerFile        # Dockerfile do PostgreSQL
├── app/                  # Aplicação Python
│   ├── Util/            # Utilitários
│   │   ├── bd.py        # Conexão com o banco de dados
│   │   └── paramsBD.yml # Configurações do banco
│   ├── models.py        # Modelos de dados
│   ├── repository.py    # Operações CRUD
│   ├── swagger.py       # API e documentação
│   └── requirements.txt # Dependências Python
├── prometheus/          # Configurações do Prometheus
├── grafana/             # Configurações do Grafana
├── dockerfile.app       # Dockerfile da Aplicação
├── dockerfile          # Dockerfile do Banco de Dados
├── compose.yml         # Configuração Docker Compose
└── init.sql            # Script de Inicialização do Banco
```

## 🔐 Variáveis de Ambiente

O sistema utiliza as seguintes variáveis de ambiente:

- FLASK_ENV: development
- FLASK_APP: app:app
- DB_HOST: db
- DB_PORT: 5432
- DB_NAME: escola
- DB_USER: user
- DB_PASSWORD: password

## 📚 Documentação da API

A API RESTful fornece os seguintes endpoints:

### Alunos

#### POST /alunos
Cria um novo aluno.

**Request Body:**
```json
{
    "nome_completo": "João Silva",
    "data_nascimento": "2010-05-15",
    "id_turma": 1,
    "nome_responsavel": "Maria Silva",
    "telefone_responsavel": "(11) 99999-9999",
    "email_responsavel": "maria@email.com",
    "endereco": "Rua A, 123",
    "cidade": "São Paulo",
    "estado": "SP",
    "cep": "01000-000",
    "pais": "Brasil",
    "telefone": "(11) 99999-9999"
}
```

#### GET /alunos/{id}
Retorna os dados de um aluno específico.

#### PUT /alunos/{id}
Atualiza os dados de um aluno.

#### DELETE /alunos/{id}
Remove um aluno.

### Professores

#### POST /professores
Cria um novo professor.

**Request Body:**
```json
{
    "nome_completo": "Maria Santos",
    "email": "maria@escola.com",
    "telefone": "(11) 99999-9999"
}
```

#### GET /professores/{id}
Retorna os dados de um professor específico.

### Turmas

#### POST /turmas
Cria uma nova turma.

**Request Body:**
```json
{
    "nome_turma": "Turma A",
    "id_professor": 1,
    "horario": "08:00 - 10:00"
}
```

#### GET /turmas/{id}
Retorna os dados de uma turma específica.

## 🤝 Contribuição

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença [MIT](LICENSE).