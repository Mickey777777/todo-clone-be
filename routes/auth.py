from flask import Blueprint, request, jsonify, session
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "username, email, password 필트가 필요합니다."
        }), 400
    
    if not all(k in data for k in ['username', 'email', 'password']):
      return jsonify({
          "success": False,
          "error": "username, email, password 필드가 필요합니다."
      }), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({
            "success": False,
            "error" : "이미 존재하는 username입니다."
        }), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({
            "success": False,
            "error" : "이미 존재하는 email입니다."
        }), 400

    new_user = User(
        username = data['username'],
        email = data['email'],
        pw_hash = generate_password_hash(data['password']),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "success": True
    }), 201

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not all(i in data for i in ['username', 'password']):
        return jsonify({
            "success": False,
            "error": "username, password 필드가 필요합니다."
        }), 400
    
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.pw_hash, data['password']):
        session['user_id'] = user.id
    else:
        return jsonify({
            "success": False,
            "error": "username또는 password가 잘못 되었습니다."
        }), 401
    
    return jsonify({
        "success": True
    }), 200

@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)

    return jsonify({
        "success": True
    }), 200
