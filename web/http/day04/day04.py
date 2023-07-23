import requests

def upload_data():
    url = "http://127.0.0.1:8080/submit/formdata"  # 上传数据的目标URL
    data = {
        "name": "sunweiming",
        "age": 18
    }  # 要上传的表单数据

    # 发送数据上传请求
    response = requests.post(url, data=data)

    # 检查响应状态码
    if response.status_code == 200:
        print(response.json())
        print("数据上传成功！")
    else:
        print("数据上传失败，状态码：", response.status_code)


if __name__ == '__main__':
    upload_data()