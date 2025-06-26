from flask import Blueprint, request, jsonify
from app.Util.bd import create_connection
from flasgger import swag_from

app = Blueprint('order_details', __name__)

@app.route('/')
def index():
    return "API para gerenciamento de detalhes de pedidos"

@app.route('/order-details', methods=['POST'])
@swag_from({
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
})
def create_order_detail():
    data = request.get_json()
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO order_details (order_id, product_id, unit_price, quantity, discount)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (data['order_id'], data['product_id'], data['unit_price'], 
             data['quantity'], data.get('discount', 0.0))
        )
        conn.commit()
        return jsonify({"message": "Order detail created successfully"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/order-details', methods=['GET'])
def get_order_details():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM order_details")
    order_details = cursor.fetchall()
    return jsonify(order_details), 200

@app.route('/order-details/<int:order_id>/<int:product_id>', methods=['GET'])
@swag_from({
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
})
def read_order_detail(order_id, product_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT order_id, product_id, unit_price, quantity, discount 
            FROM order_details 
            WHERE order_id = %s AND product_id = %s
        """, (order_id, product_id))
        order_detail = cursor.fetchone()
        
        if order_detail is None:
            return jsonify({"error": "Order detail not found"}), 404
            
        return jsonify({
            "order_id": order_detail[0],
            "product_id": order_detail[1],
            "unit_price": float(order_detail[2]),
            "quantity": order_detail[3],
            "discount": float(order_detail[4])
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/order-details/<int:order_id>/<int:product_id>', methods=['PUT'])
@swag_from({
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
                'required': ['unit_price', 'quantity'],
                'example': {
                    'unit_price': 35.99,
                    'quantity': 3,
                    'discount': 0.05
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Detalhe do pedido atualizado com sucesso'},
        400: {'description': 'Erro na requisição'}
    }
})
def update_order_detail(order_id, product_id):
    data = request.get_json()
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE order_details
            SET unit_price = %s, quantity = %s, discount = %s
            WHERE order_id = %s AND product_id = %s
            """,
            (data['unit_price'], data['quantity'], 
             data.get('discount', 0.0), order_id, product_id)
        )
        conn.commit()
        return jsonify({"message": "Order detail updated successfully"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route('/order-details/<int:order_id>/<int:product_id>', methods=['DELETE'])
@swag_from({
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
})
def delete_order_detail(order_id, product_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            DELETE FROM order_details 
            WHERE order_id = %s AND product_id = %s
        """, (order_id, product_id))
        conn.commit()
        return jsonify({"message": "Order detail deleted successfully"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Endpoint adicional para listar todos os detalhes de um pedido específico
@app.route('/order-details/<int:order_id>', methods=['GET'])
@swag_from({
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
})
def list_order_details(order_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT order_id, product_id, unit_price, quantity, discount 
            FROM order_details 
            WHERE order_id = %s
        """, (order_id,))
        order_details = cursor.fetchall()
        
        if not order_details:
            return jsonify({"error": "No order details found for this order"}), 404
            
        return jsonify([{
            "order_id": detail[0],
            "product_id": detail[1],
            "unit_price": float(detail[2]),
            "quantity": detail[3],
            "discount": float(detail[4])
        } for detail in order_details]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

 