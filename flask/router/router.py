from flask import Flask,request,jsonify

# 定义动态路由


app = Flask(__name__)

@app.route('/user/login',methods=['POST'])  # 处理json 请求
def  login():
    try:
        json_data = request.get_json()
        print(json_data)
        response_data = {"status": "success", "message": "JSON data received successfully"}
        return jsonify(response_data)
    except Exception as e:
        print(f"Error: {e}")
        response_data = {"status": "error", "message": "An error occurred while processing the request"}
        return jsonify(response_data)
def main():
    app.run(host='127.0.0.1',port=8081,debug=True)
if __name__ == '__main__':
    main()


