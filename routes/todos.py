from flask import Blueprint, jsonify, request
from datetime import datetime
import models

todos_bp = Blueprint('todos', __name__)


@todos_bp.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify({
        "success": True,
        "data": models.todos,
        "count": len(models.todos)
    })


@todos_bp.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((item for item in models.todos if item['id'] == todo_id), None)
    if todo is None:
        return jsonify({
            "success": False,
            "error": "TODO를 찾을 수 없습니다."
        }), 404

    return jsonify({
        "success": True,
        "data": todo
    })


@todos_bp.route('/api/todos', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or 'body' not in data:
        return jsonify({
            "success": False,
            "error": "body필드가 필요합니다."
        }), 400

    new_todo = {
        "id": models.id_counter,
        "user_id": "test",
        "date": datetime.now(),
        "body": data['body'],
        "status": "진행중",
        "created_at": datetime.now()
    }

    models.todos.append(new_todo)
    models.id_counter += 1

    return jsonify(new_todo)
