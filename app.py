from flask import Flask
from routes.todos import todos_bp
from models import db, User

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(todos_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db.init_app(app)

with app.app_context():
    db.create_all()

    # 테스트 유저 생성 (없으면)
    test_user = User.query.filter_by(username='test').first()
    if not test_user:
        from werkzeug.security import generate_password_hash
        test_user = User(
            username='test',
            email='test@example.com',
            pw_hash=generate_password_hash('test1234')
        )
        db.session.add(test_user)
        db.session.commit()
        print("✅ 테스트 유저 생성됨 (username: test, password: test1234)")

if __name__ == '__main__':
    app.run(debug=True)
