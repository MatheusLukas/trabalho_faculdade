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
