from flask import Blueprint, request, jsonify
from app.Util.bd import create_connection
from flasgger import swag_from
from app.swagger import categories_docs
import base64

app = Blueprint('categories', __name__)

@app.route('/categories', methods=['POST'])
@swag_from(categories_docs['create_category'])
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
@swag_from(categories_docs['read_category'])
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
@swag_from(categories_docs['update_category'])
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
@swag_from(categories_docs['delete_category'])
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

