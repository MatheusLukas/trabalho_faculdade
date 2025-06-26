from flask import Blueprint, request, jsonify
from app.Util.bd import create_connection
from flasgger import swag_from
from app.swagger import professores_docs

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['POST'])
@swag_from(professores_docs['create_professor'])
def create_professor():
    data = request.get_json()
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO professor (nome_completo, email, telefone)
            VALUES (%s, %s, %s)
            """,
            (data['nome_completo'], data.get('email'), data.get('telefone'))
        )
        conn.commit()
        return jsonify({"message": "Professor criado com sucesso"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@professores_bp.route('/professores/<int:id_professor>', methods=['GET'])
@swag_from(professores_docs['read_professor'])
def read_professor(id_professor):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM professor WHERE id_professor = %s", (id_professor,))
        professor = cursor.fetchone()
        if professor is None:
            return jsonify({"error": "Professor não encontrado"}), 404
        return jsonify({
            "id_professor": professor[0],
            "nome_completo": professor[1],
            "email": professor[2],
            "telefone": professor[3]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@professores_bp.route('/professores', methods=['GET'])
@swag_from(professores_docs['read_all_professores'])
def read_all_professores():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM professor ORDER BY nome_completo")
        professores = cursor.fetchall()
        
        result = []
        for professor in professores:
            result.append({
                "id_professor": professor[0],
                "nome_completo": professor[1],
                "email": professor[2],
                "telefone": professor[3]
            })
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@professores_bp.route('/professores/<int:id_professor>', methods=['PUT'])
@swag_from(professores_docs['update_professor'])
def update_professor(id_professor):
    data = request.get_json()
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE professor
            SET nome_completo = %s, email = %s, telefone = %s
            WHERE id_professor = %s
            """,
            (data['nome_completo'], data.get('email'), data.get('telefone'), id_professor)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Professor não encontrado"}), 404
        return jsonify({"message": "Professor atualizado com sucesso"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

@professores_bp.route('/professores/<int:id_professor>', methods=['DELETE'])
@swag_from(professores_docs['delete_professor'])
def delete_professor(id_professor):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM professor WHERE id_professor = %s", (id_professor,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Professor não encontrado"}), 404
        return jsonify({"message": "Professor deletado com sucesso"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        cursor.close()
        conn.close() 