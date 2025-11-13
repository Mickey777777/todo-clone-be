from flask import Flask
from routes.todos import todos_bp

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(todos_bp)


if __name__ == '__main__':
    app.run(debug=True)
