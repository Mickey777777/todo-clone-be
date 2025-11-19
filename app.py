from flask import Flask
from routes.todos import todos_bp
from models import db, User
from routes.auth import auth_bp
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(todos_bp)
app.register_blueprint(auth_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
