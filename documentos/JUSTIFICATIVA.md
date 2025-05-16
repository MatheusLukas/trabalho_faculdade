# Documentação do Modelo Entidade-Relacionamento (MER) - Sistema de Gestão Escolar

O sistema foi modelado com base em um cenário de **gestão escolar**, identificando as principais entidades:

- **Professor**
- **Turma**
- **Aluno**
- **Pagamento**
- **Presença**
- **Atividade**
- **Usuário**

Cada entidade representa um elemento real do contexto acadêmico, com atributos definidos de acordo com suas propriedades.

## Relacionamentos e Regras do Negócio

- Um **professor** pode ministrar várias **turmas** (**1:N**).
- Um **aluno** pertence a uma **turma** (**N:1**).
- Cada **aluno** pode ter múltiplos registros de **presença** (**1:N**) e **pagamentos** (**1:N**).
- As **atividades** realizadas por **alunos** formam uma relação **N:N** (através da tabela de associação `atividade_aluno`).
- **Usuários** podem ser vinculados a **professores** para controle de acesso ao sistema (**1:N**, opcional).

## Considerações de Modelagem

- As **chaves primárias (PK)** garantem a unicidade dos registros.
- As **chaves estrangeiras (FK)** asseguram a integridade referencial entre as tabelas.
- A modelagem foi **normalizada até a 3FN (Terceira Forma Normal)**, evitando redundâncias e facilitando a manutenção do banco de dados.
