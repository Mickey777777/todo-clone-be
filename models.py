from datetime import datetime

# 메모리에 저장할 todos 리스트
todos = [
    {'id': 1, 'user_id': 'test', 'date': datetime.now(), 'body': 'test123123', 'status': '진행중', 'created_at': datetime.now()},
    {'id': 2, 'user_id': 'test', 'date': datetime.now(), 'body': 'test123123123123', 'status': '진행중', 'created_at': datetime.now()}
]

# ID 카운터
id_counter = 3
