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
    print(name,age)
    # 进行数据处理或业务逻辑
    # ...
    # 返回处理后的结果
    result = {
        "name": name,
        "age": age
    }
    return jsonify(result)
# curl localhost:8080/api/data -X POST -d '{"hello": "world"}' --header "Content-Type: application/json"
@app.route('/api/data', methods=['POST'])
def update_data():
    new_data = request.get_json()  # 获取POST请求中的JSON数据
    print(new_data)
    return jsonify(new_data)


# curl "http://127.0.0.1:8080/api/data?name=John&age=30"


@app.route('/submit/x-www-form-urlencode', methods=['POST'])
def submit_xwwwformurlencod():
    # Get form parameters
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(name,email,message)
    # Perform data processing or business logic here (if needed)
    # ...
    # Prepare response data
    response_data = {
        "name": name,
        "email": email,
        "message": message
    }
    return jsonify(response_data)
# curl -X POST -d "name=John&email=john@example.com&message=Hello" http://127.0.0.1:8080/submit


@app.route('/submit/formdata', methods=['POST'])
def submit_formdata():
    # Get form parameters
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Perform data processing or business logic here (if needed)
    # ...

    # Prepare response data
    response_data = {
        "name": name,
        "email": email,
        "message": message
    }

    return jsonify(response_data)
# curl -X POST -F "name=sunweiming" -F "email=1319847957qq.com" -F "message=Hello" http://127.0.0.1:8080/submit/formdata
if __name__ == '__main__':
    app.run(debug=True,port=8080)
