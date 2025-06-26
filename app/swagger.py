from flasgger import Swagger

def init_swagger(app):
    """
    Initialize Swagger for the Flask app
    """
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Gestão Escolar",
            "version": "1.0.0",
            "description": "API para gestão de alunos, categorias e detalhes de pedidos",
            "termsOfService": "",
            "contact": {
                "email": "contato@escola.com"
            },
            "license": {
                "name": "MIT",
                "url": "https://opensource.org/licenses/MIT"
            }
        }
    }
    
    swagger = Swagger(app, config=swagger_config, template=swagger_template)
    return swagger

# Documentação para CRUD Alunos
alunos_docs = {
    'create_aluno': {
        'tags': ['Alunos'],
        'description': 'Cria um novo aluno.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome_completo': {'type': 'string', 'description': 'Nome completo do aluno'},
                    'data_nascimento': {'type': 'string', 'format': 'date', 'description': 'Data de nascimento'},
                    'id_turma': {'type': 'integer', 'description': 'ID da turma'},
                    'nome_responsavel': {'type': 'string', 'description': 'Nome do responsável'},
                    'telefone_responsavel': {'type': 'string', 'description': 'Telefone do responsável'},
                    'email_responsavel': {'type': 'string', 'description': 'Email do responsável'},
                    'informacoes_adicionais': {'type': 'string', 'description': 'Informações adicionais'},
                    'endereco': {'type': 'string', 'description': 'Endereço do aluno'},
                    'cidade': {'type': 'string', 'description': 'Cidade do aluno'},
                    'estado': {'type': 'string', 'description': 'Estado do aluno'},
                    'cep': {'type': 'string', 'description': 'CEP do aluno'},
                    'pais': {'type': 'string', 'description': 'País do aluno'},
                    'telefone': {'type': 'string', 'description': 'Telefone do aluno'}
                },
                'required': ['nome_completo', 'data_nascimento'],
                'example': {
                    'nome_completo': 'João Silva',
                    'data_nascimento': '2010-05-15',
                    'id_turma': 1,
                    'nome_responsavel': 'Maria Silva',
                    'telefone_responsavel': '(11) 98888-8888',
                    'email_responsavel': 'maria@email.com',
                    'endereco': 'Rua das Flores, 123',
                    'cidade': 'São Paulo',
                    'estado': 'SP',
                    'cep': '01234-567',
                    'pais': 'Brasil',
                    'telefone': '(11) 99999-9999'
                }
            }
        }],
        'responses': {
            201: {'description': 'Aluno criado com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_aluno': {
        'tags': ['Alunos'],
        'description': 'Busca um aluno pelo ID.',
        'parameters': [{
            'name': 'id_aluno',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do aluno'
        }],
        'responses': {
            200: {
                'description': 'Dados do aluno',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id_aluno': {'type': 'integer'},
                        'nome_completo': {'type': 'string'},
                        'data_nascimento': {'type': 'string', 'format': 'date'},
                        'id_turma': {'type': 'integer'},
                        'nome_responsavel': {'type': 'string'},
                        'telefone_responsavel': {'type': 'string'},
                        'email_responsavel': {'type': 'string'},
                        'informacoes_adicionais': {'type': 'string'},
                        'endereco': {'type': 'string'},
                        'cidade': {'type': 'string'},
                        'estado': {'type': 'string'},
                        'cep': {'type': 'string'},
                        'pais': {'type': 'string'},
                        'telefone': {'type': 'string'}
                    }
                }
            },
            404: {'description': 'Aluno não encontrado'}
        }
    },
    'read_all_alunos': {
        'tags': ['Alunos'],
        'description': 'Lista todos os alunos cadastrados.',
        'responses': {
            200: {
                'description': 'Lista de alunos',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id_aluno': {'type': 'integer'},
                            'nome_completo': {'type': 'string'},
                            'data_nascimento': {'type': 'string', 'format': 'date'},
                            'id_turma': {'type': 'integer'},
                            'nome_responsavel': {'type': 'string'},
                            'telefone_responsavel': {'type': 'string'},
                            'email_responsavel': {'type': 'string'},
                            'informacoes_adicionais': {'type': 'string'},
                            'endereco': {'type': 'string'},
                            'cidade': {'type': 'string'},
                            'estado': {'type': 'string'},
                            'cep': {'type': 'string'},
                            'pais': {'type': 'string'},
                            'telefone': {'type': 'string'}
                        }
                    }
                }
            }
        }
    },
    'update_aluno': {
        'tags': ['Alunos'],
        'description': 'Atualiza os dados de um aluno.',
        'parameters': [
            {
                'name': 'id_aluno',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do aluno'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'nome_completo': {'type': 'string'},
                        'data_nascimento': {'type': 'string', 'format': 'date'},
                        'id_turma': {'type': 'integer'},
                        'nome_responsavel': {'type': 'string'},
                        'telefone_responsavel': {'type': 'string'},
                        'email_responsavel': {'type': 'string'},
                        'informacoes_adicionais': {'type': 'string'},
                        'endereco': {'type': 'string'},
                        'cidade': {'type': 'string'},
                        'estado': {'type': 'string'},
                        'cep': {'type': 'string'},
                        'pais': {'type': 'string'},
                        'telefone': {'type': 'string'}
                    },
                    'required': ['nome_completo', 'data_nascimento']
                }
            }
        ],
        'responses': {
            200: {'description': 'Aluno atualizado com sucesso'},
            404: {'description': 'Aluno não encontrado'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_aluno': {
        'tags': ['Alunos'],
        'description': 'Remove um aluno pelo ID.',
        'parameters': [{
            'name': 'id_aluno',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do aluno'
        }],
        'responses': {
            200: {'description': 'Aluno deletado com sucesso'},
            404: {'description': 'Aluno não encontrado'}
        }
    }
}

# Documentação para CRUD Categorias
categories_docs = {
    'create_category': {
        'tags': ['Categorias'],
        'description': 'Cria uma nova categoria.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'category_id': {'type': 'integer', 'description': 'ID único da categoria'},
                    'category_name': {'type': 'string', 'description': 'Nome da categoria'},
                    'description': {'type': 'string', 'description': 'Descrição da categoria'},
                    'picture': {'type': 'string', 'description': 'Imagem da categoria (base64)'}
                },
                'required': ['category_id', 'category_name'],
                'example': {
                    'category_id': 1,
                    'category_name': 'Eletrônicos',
                    'description': 'Produtos eletrônicos diversos',
                    'picture': "https://cdn.pixabay.com/photo/2025/04/19/18/20/goose-9544312_1280.jpg"
                }
            }
        }],
        'responses': {
            201: {'description': 'Categoria criada com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_category': {
        'tags': ['Categorias'],
        'description': 'Busca uma categoria pelo ID.',
        'parameters': [{
            'name': 'category_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da categoria'
        }],
        'responses': {
            200: {
                'description': 'Dados da categoria',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'category_id': {'type': 'integer'},
                        'category_name': {'type': 'string'},
                        'description': {'type': 'string'},
                        'picture': {'type': 'string'}
                    }
                }
            },
            404: {'description': 'Categoria não encontrada'}
        }
    },
    'update_category': {
        'tags': ['Categorias'],
        'description': 'Atualiza os dados de uma categoria.',
        'parameters': [
            {
                'name': 'category_id',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID da categoria'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'category_name': {'type': 'string'},
                        'description': {'type': 'string'},
                        'picture': {'type': 'string'}
                    },
                    'required': ['category_name']
                }
            }
        ],
        'responses': {
            200: {'description': 'Categoria atualizada com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_category': {
        'tags': ['Categorias'],
        'description': 'Remove uma categoria pelo ID.',
        'parameters': [{
            'name': 'category_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da categoria'
        }],
        'responses': {
            200: {'description': 'Categoria deletada com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    }
}

# Documentação para CRUD Order Details
order_details_docs = {
    'create_order_detail': {
        'tags': ['Detalhes do Pedido'],
        'description': 'Cria um novo detalhe de pedido.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'order_id': {'type': 'integer', 'description': 'ID do pedido'},
                    'product_id': {'type': 'integer', 'description': 'ID do produto'},
                    'unit_price': {'type': 'number', 'description': 'Preço unitário'},
                    'quantity': {'type': 'integer', 'description': 'Quantidade'},
                    'discount': {'type': 'number', 'description': 'Desconto aplicado (0.0 a 1.0)'}
                },
                'required': ['order_id', 'product_id', 'unit_price', 'quantity'],
                'example': {
                    'order_id': 1,
                    'product_id': 10,
                    'unit_price': 29.99,
                    'quantity': 2,
                    'discount': 0.1
                }
            }
        }],
        'responses': {
            201: {'description': 'Detalhe do pedido criado com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_order_detail': {
        'tags': ['Detalhes do Pedido'],
        'description': 'Busca um detalhe de pedido específico.',
        'parameters': [
            {
                'name': 'order_id',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do pedido'
            },
            {
                'name': 'product_id',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do produto'
            }
        ],
        'responses': {
            200: {
                'description': 'Dados do detalhe do pedido',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'order_id': {'type': 'integer'},
                        'product_id': {'type': 'integer'},
                        'unit_price': {'type': 'number'},
                        'quantity': {'type': 'integer'},
                        'discount': {'type': 'number'}
                    }
                }
            },
            404: {'description': 'Detalhe do pedido não encontrado'}
        }
    },
    'list_order_details': {
        'tags': ['Detalhes do Pedido'],
        'description': 'Lista todos os detalhes de um pedido específico.',
        'parameters': [{
            'name': 'order_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do pedido'
        }],
        'responses': {
            200: {
                'description': 'Lista de detalhes do pedido',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'order_id': {'type': 'integer'},
                            'product_id': {'type': 'integer'},
                            'unit_price': {'type': 'number'},
                            'quantity': {'type': 'integer'},
                            'discount': {'type': 'number'}
                        }
                    }
                }
            },
            404: {'description': 'Nenhum detalhe encontrado para este pedido'}
        }
    },
    'update_order_detail': {
        'tags': ['Detalhes do Pedido'],
        'description': 'Atualiza um detalhe de pedido.',
        'parameters': [
            {
                'name': 'order_id',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do pedido'
            },
            {
                'name': 'product_id',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do produto'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'unit_price': {'type': 'number'},
                        'quantity': {'type': 'integer'},
                        'discount': {'type': 'number'}
                    },
                    'required': ['unit_price', 'quantity']
                }
            }
        ],
        'responses': {
            200: {'description': 'Detalhe do pedido atualizado com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_order_detail': {
        'tags': ['Detalhes do Pedido'],
        'description': 'Remove um detalhe de pedido.',
        'parameters': [
            {
                'name': 'order_id',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do pedido'
            },
            {
                'name': 'product_id',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do produto'
            }
        ],
        'responses': {
            200: {'description': 'Detalhe do pedido deletado com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    }
}

# Documentação para CRUD Turmas
turmas_docs = {
    'create_turma': {
        'tags': ['Turmas'],
        'description': 'Cria uma nova turma.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome_turma': {'type': 'string', 'description': 'Nome da turma'},
                    'id_professor': {'type': 'integer', 'description': 'ID do professor'},
                    'horario': {'type': 'string', 'description': 'Horário da turma'}
                },
                'required': ['nome_turma'],
                'example': {
                    'nome_turma': 'Turma A - 1º Ano',
                    'id_professor': 1,
                    'horario': 'Segunda a Sexta - 08:00 às 12:00'
                }
            }
        }],
        'responses': {
            201: {'description': 'Turma criada com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_turma': {
        'tags': ['Turmas'],
        'description': 'Busca uma turma pelo ID.',
        'parameters': [{
            'name': 'id_turma',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da turma'
        }],
        'responses': {
            200: {'description': 'Dados da turma'},
            404: {'description': 'Turma não encontrada'}
        }
    },
    'read_all_turmas': {
        'tags': ['Turmas'],
        'description': 'Lista todas as turmas.',
        'responses': {
            200: {'description': 'Lista de turmas'}
        }
    },
    'update_turma': {
        'tags': ['Turmas'],
        'description': 'Atualiza os dados de uma turma.',
        'parameters': [
            {
                'name': 'id_turma',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID da turma'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'nome_turma': {'type': 'string'},
                        'id_professor': {'type': 'integer'},
                        'horario': {'type': 'string'}
                    },
                    'required': ['nome_turma']
                }
            }
        ],
        'responses': {
            200: {'description': 'Turma atualizada com sucesso'},
            404: {'description': 'Turma não encontrada'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_turma': {
        'tags': ['Turmas'],
        'description': 'Remove uma turma pelo ID.',
        'parameters': [{
            'name': 'id_turma',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da turma'
        }],
        'responses': {
            200: {'description': 'Turma deletada com sucesso'},
            404: {'description': 'Turma não encontrada'}
        }
    }
}

# Documentação para CRUD Professores
professores_docs = {
    'create_professor': {
        'tags': ['Professores'],
        'description': 'Cria um novo professor.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nome_completo': {'type': 'string', 'description': 'Nome completo do professor'},
                    'email': {'type': 'string', 'description': 'Email do professor'},
                    'telefone': {'type': 'string', 'description': 'Telefone do professor'}
                },
                'required': ['nome_completo'],
                'example': {
                    'nome_completo': 'Ana Santos',
                    'email': 'ana.santos@escola.com',
                    'telefone': '(11) 98765-4321'
                }
            }
        }],
        'responses': {
            201: {'description': 'Professor criado com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_professor': {
        'tags': ['Professores'],
        'description': 'Busca um professor pelo ID.',
        'parameters': [{
            'name': 'id_professor',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do professor'
        }],
        'responses': {
            200: {'description': 'Dados do professor'},
            404: {'description': 'Professor não encontrado'}
        }
    },
    'read_all_professores': {
        'tags': ['Professores'],
        'description': 'Lista todos os professores.',
        'responses': {
            200: {'description': 'Lista de professores'}
        }
    },
    'update_professor': {
        'tags': ['Professores'],
        'description': 'Atualiza os dados de um professor.',
        'parameters': [
            {
                'name': 'id_professor',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do professor'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'nome_completo': {'type': 'string'},
                        'email': {'type': 'string'},
                        'telefone': {'type': 'string'}
                    },
                    'required': ['nome_completo']
                }
            }
        ],
        'responses': {
            200: {'description': 'Professor atualizado com sucesso'},
            404: {'description': 'Professor não encontrado'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_professor': {
        'tags': ['Professores'],
        'description': 'Remove um professor pelo ID.',
        'parameters': [{
            'name': 'id_professor',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do professor'
        }],
        'responses': {
            200: {'description': 'Professor deletado com sucesso'},
            404: {'description': 'Professor não encontrado'}
        }
    }
}

# Documentação para CRUD Pagamentos
pagamentos_docs = {
    'create_pagamento': {
        'tags': ['Pagamentos'],
        'description': 'Cria um novo pagamento.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id_aluno': {'type': 'integer', 'description': 'ID do aluno'},
                    'data_pagamento': {'type': 'string', 'format': 'date', 'description': 'Data do pagamento'},
                    'valor_pago': {'type': 'number', 'description': 'Valor pago'},
                    'forma_pagamento': {'type': 'string', 'description': 'Forma de pagamento'},
                    'referencia': {'type': 'string', 'description': 'Referência do pagamento'},
                    'status': {'type': 'string', 'description': 'Status do pagamento'}
                },
                'required': ['id_aluno', 'data_pagamento', 'valor_pago'],
                'example': {
                    'id_aluno': 1,
                    'data_pagamento': '2024-01-15',
                    'valor_pago': 350.00,
                    'forma_pagamento': 'PIX',
                    'referencia': 'Janeiro/2024',
                    'status': 'Pago'
                }
            }
        }],
        'responses': {
            201: {'description': 'Pagamento criado com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_pagamento': {
        'tags': ['Pagamentos'],
        'description': 'Busca um pagamento pelo ID.',
        'parameters': [{
            'name': 'id_pagamento',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do pagamento'
        }],
        'responses': {
            200: {'description': 'Dados do pagamento'},
            404: {'description': 'Pagamento não encontrado'}
        }
    },
    'read_all_pagamentos': {
        'tags': ['Pagamentos'],
        'description': 'Lista todos os pagamentos.',
        'responses': {
            200: {'description': 'Lista de pagamentos'}
        }
    },
    'update_pagamento': {
        'tags': ['Pagamentos'],
        'description': 'Atualiza os dados de um pagamento.',
        'parameters': [
            {
                'name': 'id_pagamento',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do pagamento'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id_aluno': {'type': 'integer'},
                        'data_pagamento': {'type': 'string', 'format': 'date'},
                        'valor_pago': {'type': 'number'},
                        'forma_pagamento': {'type': 'string'},
                        'referencia': {'type': 'string'},
                        'status': {'type': 'string'}
                    },
                    'required': ['id_aluno', 'data_pagamento', 'valor_pago']
                }
            }
        ],
        'responses': {
            200: {'description': 'Pagamento atualizado com sucesso'},
            404: {'description': 'Pagamento não encontrado'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_pagamento': {
        'tags': ['Pagamentos'],
        'description': 'Remove um pagamento pelo ID.',
        'parameters': [{
            'name': 'id_pagamento',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do pagamento'
        }],
        'responses': {
            200: {'description': 'Pagamento deletado com sucesso'},
            404: {'description': 'Pagamento não encontrado'}
        }
    }
}

# Documentação para CRUD Presenças
presencas_docs = {
    'create_presenca': {
        'tags': ['Presenças'],
        'description': 'Cria um novo registro de presença.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id_aluno': {'type': 'integer', 'description': 'ID do aluno'},
                    'data_presenca': {'type': 'string', 'format': 'date', 'description': 'Data da presença'},
                    'presente': {'type': 'boolean', 'description': 'Se o aluno esteve presente'}
                },
                'required': ['id_aluno', 'data_presenca', 'presente'],
                'example': {
                    'id_aluno': 1,
                    'data_presenca': '2024-01-15',
                    'presente': True
                }
            }
        }],
        'responses': {
            201: {'description': 'Presença criada com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_presenca': {
        'tags': ['Presenças'],
        'description': 'Busca uma presença pelo ID.',
        'parameters': [{
            'name': 'id_presenca',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da presença'
        }],
        'responses': {
            200: {'description': 'Dados da presença'},
            404: {'description': 'Presença não encontrada'}
        }
    },
    'read_all_presencas': {
        'tags': ['Presenças'],
        'description': 'Lista todas as presenças.',
        'responses': {
            200: {'description': 'Lista de presenças'}
        }
    },
    'update_presenca': {
        'tags': ['Presenças'],
        'description': 'Atualiza os dados de uma presença.',
        'parameters': [
            {
                'name': 'id_presenca',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID da presença'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id_aluno': {'type': 'integer'},
                        'data_presenca': {'type': 'string', 'format': 'date'},
                        'presente': {'type': 'boolean'}
                    },
                    'required': ['id_aluno', 'data_presenca', 'presente']
                }
            }
        ],
        'responses': {
            200: {'description': 'Presença atualizada com sucesso'},
            404: {'description': 'Presença não encontrada'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_presenca': {
        'tags': ['Presenças'],
        'description': 'Remove uma presença pelo ID.',
        'parameters': [{
            'name': 'id_presenca',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da presença'
        }],
        'responses': {
            200: {'description': 'Presença deletada com sucesso'},
            404: {'description': 'Presença não encontrada'}
        }
    }
}

# Documentação para CRUD Atividades
atividades_docs = {
    'create_atividade': {
        'tags': ['Atividades'],
        'description': 'Cria uma nova atividade.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'descricao': {'type': 'string', 'description': 'Descrição da atividade'},
                    'data_realizacao': {'type': 'string', 'format': 'date', 'description': 'Data de realização'}
                },
                'required': ['descricao', 'data_realizacao'],
                'example': {
                    'descricao': 'Prova de Matemática - Frações',
                    'data_realizacao': '2024-01-20'
                }
            }
        }],
        'responses': {
            201: {'description': 'Atividade criada com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_atividade': {
        'tags': ['Atividades'],
        'description': 'Busca uma atividade pelo ID.',
        'parameters': [{
            'name': 'id_atividade',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da atividade'
        }],
        'responses': {
            200: {'description': 'Dados da atividade'},
            404: {'description': 'Atividade não encontrada'}
        }
    },
    'read_all_atividades': {
        'tags': ['Atividades'],
        'description': 'Lista todas as atividades.',
        'responses': {
            200: {'description': 'Lista de atividades'}
        }
    },
    'update_atividade': {
        'tags': ['Atividades'],
        'description': 'Atualiza os dados de uma atividade.',
        'parameters': [
            {
                'name': 'id_atividade',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID da atividade'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'descricao': {'type': 'string'},
                        'data_realizacao': {'type': 'string', 'format': 'date'}
                    },
                    'required': ['descricao', 'data_realizacao']
                }
            }
        ],
        'responses': {
            200: {'description': 'Atividade atualizada com sucesso'},
            404: {'description': 'Atividade não encontrada'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_atividade': {
        'tags': ['Atividades'],
        'description': 'Remove uma atividade pelo ID.',
        'parameters': [{
            'name': 'id_atividade',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID da atividade'
        }],
        'responses': {
            200: {'description': 'Atividade deletada com sucesso'},
            404: {'description': 'Atividade não encontrada'}
        }
    }
}

# Documentação para CRUD Atividades-Alunos
atividades_alunos_docs = {
    'create_atividade_aluno': {
        'tags': ['Atividades-Alunos'],
        'description': 'Cria uma nova associação atividade-aluno.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id_atividade': {'type': 'integer', 'description': 'ID da atividade'},
                    'id_aluno': {'type': 'integer', 'description': 'ID do aluno'}
                },
                'required': ['id_atividade', 'id_aluno'],
                'example': {
                    'id_atividade': 1,
                    'id_aluno': 1
                }
            }
        }],
        'responses': {
            201: {'description': 'Atividade-Aluno criada com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_atividade_aluno': {
        'tags': ['Atividades-Alunos'],
        'description': 'Busca uma associação atividade-aluno.',
        'parameters': [
            {
                'name': 'id_atividade',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID da atividade'
            },
            {
                'name': 'id_aluno',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do aluno'
            }
        ],
        'responses': {
            200: {'description': 'Dados da associação'},
            404: {'description': 'Associação não encontrada'}
        }
    },
    'read_all_atividades_alunos': {
        'tags': ['Atividades-Alunos'],
        'description': 'Lista todas as associações atividade-aluno.',
        'responses': {
            200: {'description': 'Lista de associações'}
        }
    },
    'delete_atividade_aluno': {
        'tags': ['Atividades-Alunos'],
        'description': 'Remove uma associação atividade-aluno.',
        'parameters': [
            {
                'name': 'id_atividade',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID da atividade'
            },
            {
                'name': 'id_aluno',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do aluno'
            }
        ],
        'responses': {
            200: {'description': 'Associação deletada com sucesso'},
            404: {'description': 'Associação não encontrada'}
        }
    }
}

# Documentação para CRUD Usuários
usuarios_docs = {
    'create_usuario': {
        'tags': ['Usuários'],
        'description': 'Cria um novo usuário.',
        'parameters': [{
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'login': {'type': 'string', 'description': 'Login do usuário'},
                    'senha': {'type': 'string', 'description': 'Senha do usuário'},
                    'nivel_acesso': {'type': 'string', 'description': 'Nível de acesso'},
                    'id_professor': {'type': 'integer', 'description': 'ID do professor (opcional)'}
                },
                'required': ['login', 'senha'],
                'example': {
                    'login': 'admin',
                    'senha': 'senha123',
                    'nivel_acesso': 'administrador',
                    'id_professor': 1
                }
            }
        }],
        'responses': {
            201: {'description': 'Usuário criado com sucesso'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'read_usuario': {
        'tags': ['Usuários'],
        'description': 'Busca um usuário pelo ID.',
        'parameters': [{
            'name': 'id_usuario',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do usuário'
        }],
        'responses': {
            200: {'description': 'Dados do usuário'},
            404: {'description': 'Usuário não encontrado'}
        }
    },
    'read_all_usuarios': {
        'tags': ['Usuários'],
        'description': 'Lista todos os usuários.',
        'responses': {
            200: {'description': 'Lista de usuários'}
        }
    },
    'update_usuario': {
        'tags': ['Usuários'],
        'description': 'Atualiza os dados de um usuário.',
        'parameters': [
            {
                'name': 'id_usuario',
                'in': 'path',
                'required': True,
                'type': 'integer',
                'description': 'ID do usuário'
            },
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'login': {'type': 'string'},
                        'senha': {'type': 'string'},
                        'nivel_acesso': {'type': 'string'},
                        'id_professor': {'type': 'integer'}
                    },
                    'required': ['login', 'senha']
                }
            }
        ],
        'responses': {
            200: {'description': 'Usuário atualizado com sucesso'},
            404: {'description': 'Usuário não encontrado'},
            400: {'description': 'Erro na requisição'}
        }
    },
    'delete_usuario': {
        'tags': ['Usuários'],
        'description': 'Remove um usuário pelo ID.',
        'parameters': [{
            'name': 'id_usuario',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID do usuário'
        }],
        'responses': {
            200: {'description': 'Usuário deletado com sucesso'},
            404: {'description': 'Usuário não encontrado'}
        }
    }
}

