from flask import Blueprint, jsonify, request
from datetime import datetime
from models import db, User, Todo

todos_bp = Blueprint('todos', __name__)


@todos_bp.route('/api/todos', methods=['GET'])
def get_todos():
    user = User.query.filter_by(username='test').first()
    
    if not user:
        return jsonify({
            "success": False,
            "error": "유저를 찾을 수 없습니다."
        }), 404
    
    todos = Todo.query.filter_by(user_id=user.id).all()

    return jsonify({
        "success": True,
        "data": [todo.to_dict() for todo in todos],
        "count": len(todos)
    })


@todos_bp.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    user = User.query.filter_by(username='test').first()
    if not user:
        return jsonify({
            "success": False,
            "error": "유저를 찾을 수 없습니다."
        }), 404
    
    todo = Todo.query.filter_by(user_id=user.id).filter_by(id=todo_id).first()

    if not todo:
        return jsonify({
            "success": False,
            "error": "투두를 찾을 수 없습니다."
        }), 404

    return jsonify({
        "success": True,
        "data": todo.to_dict()
    })


@todos_bp.route('/api/todos', methods=['POST'])
def create_post():
    user = User.query.filter_by(username='test').first()
    if not user:
        return jsonify({
            "success": False,
            "error": "유저를 찾을 수 없습니다."
        }), 404

    data = request.get_json()
    if not data or 'body' not in data:
        return jsonify({
            "success": False,
            "error": "body필드가 필요합니다."
        }), 400

    new_todo = Todo(
        user_id = user.id,
        date =datetime.now(),
        body = data['body'],
        status = "진행중",
        created_at = datetime.now()
    )

    db.session.add(new_todo)
    db.session.commit()

    return jsonify({
        "success": True,
        "data": new_todo.to_dict()
    }), 201
