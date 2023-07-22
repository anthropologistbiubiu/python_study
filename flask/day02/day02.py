# import requests
# flask 获取 json 请求
from flask import Flask, jsonify, request

app = Flask(__name__)

# 假设这是后端的数据
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def update_data():
    new_data = request.get_json()  # 获取POST请求中的JSON数据
    data.update(new_data)         # 更新数据
    return jsonify(data)

if __name__ == '__main__':
    app.run()
