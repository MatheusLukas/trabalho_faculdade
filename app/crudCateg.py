from flask import Blueprint, request, jsonify
from app.Util.bd import create_connection
from flasgger import swag_from
import base64

app = Blueprint('categories', __name__)

@app.route('/categories', methods=['POST'])
@swag_from({
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
                'picture': None
            }
        }
    }],
    'responses': {
        201: {'description': 'Categoria criada com sucesso'},
        400: {'description': 'Erro na requisição'}
    }
})
def create_category():
    data = request.get_json()
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO categories (category_id, category_name, description, picture)
            VALUES (%s, %s, %s, %s)
            """,
            (data['category_id'], data['category_name'], data.get('description'), data.get('picture'))
        )
        conn.commit()
        return jsonify({"message": "Category created successfully"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/categories', methods=['GET'])
def get_categories():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    return jsonify(categories), 200

@app.route('/categories/<int:category_id>', methods=['GET'])
@swag_from({
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
})
def read_category(category_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM categories WHERE category_id = %s", (category_id,))
        category = cursor.fetchone()
        if category is None:
            return jsonify({"error": "Category not found"}), 404
        return jsonify({
            "category_id": category[0],
            "category_name": category[1],
            "description": category[2],
            "picture": base64.b64encode(category[3]).decode('utf-8') if category[3] else None,
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/categories/<int:category_id>', methods=['PUT'])
@swag_from({
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
                'required': ['category_name'],
                'example': {
                    'category_name': 'Eletrodomésticos',
                    'description': 'Produtos para casa',
                    'picture': None
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Categoria atualizada com sucesso'},
        400: {'description': 'Erro na requisição'}
    }
})
def update_category(category_id):
    data = request.get_json()
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE categories
            SET category_name = %s, description = %s, picture = %s
            WHERE category_id = %s
            """,
            (data['category_name'], data.get('description'), data.get('picture'), category_id)
        )
        conn.commit()
        return jsonify({"message": "Category updated successfully"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/categories/<int:category_id>', methods=['DELETE'])
@swag_from({
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
})
def delete_category(category_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM categories WHERE category_id = %s", (category_id,))
        conn.commit()
        return jsonify({"message": "Category deleted successfully"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

