from flask import Flask, render_template, send_from_directory
from routes.todos import todos_bp

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(todos_bp)


# 프론트엔드 서빙
@app.route('/')
def index():
    return render_template('index.html')


# assets 파일 서빙 (Vite 빌드 파일)
@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('static/assets', path)


if __name__ == '__main__':
    app.run(debug=True)
