"""
import requests as req

r = req.get('http://www.baidu.com')

print(r.text)[0:300]
"""
import http.client

def http_client_demo():
    # 服务器信息
    host = "www.example.com"
    port = 80
    url = "/api/data"  # 请求的路径

    # 创建HTTP连接
    conn = http.client.HTTPConnection(host, port)

    try:
        # 发送GET请求
        conn.request("GET", url)

        # 获取响应
        response = conn.getresponse()

        # 检查响应状态码
        if response.status == 200:
            # 读取响应内容
            data = response.read()

            # 打印响应内容
            print(data.decode('utf-8'))
        else:
            print("请求失败，状态码：", response.status)

    except http.client.HTTPException as e:
        print("HTTP异常：", e)
    except Exception as e:
        print("其他异常：", e)
    finally:
        # 关闭连接
        conn.close()

if __name__ == "__main__":
    http_client_demo()
