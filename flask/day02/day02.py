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
    # 获取GET请求中的query参数
    name = request.args.get('name')
    age = request.args.get('age')

    # 进行数据处理或业务逻辑
    # ...

    # 返回处理后的结果
    result = {
        "name": name,
        "age": age
    }
    return jsonify(result)

@app.route('/api/data', methods=['POST'])
def update_data():
    new_data = request.get_json()  # 获取POST请求中的JSON数据
    print(new_data)
    data.update(new_data)         # 更新数据
    print("data",data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
