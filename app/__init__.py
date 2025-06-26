# Arquivo __init__.py para tornar a pasta app um pacote Python.
from flask import Flask, jsonify, redirect

def create_app():
    app = Flask(__name__)
    
    # Registrar todos os blueprints dos CRUDs
    from app.crudAlunos import app as alunos_app
    from app.crudCateg import app as categories_app
    from app.crudOrderDetails import app as order_details_app
    
    app.register_blueprint(alunos_app)
    app.register_blueprint(categories_app)
    app.register_blueprint(order_details_app)
    
    # Inicializar Swagger para documentação da API
    from app.swagger import init_swagger
    init_swagger(app)
    
    return app 