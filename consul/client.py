import requests
import consul

# 初始化 Consul 客户端
c = consul.Consul()

# 获取服务地址
index, services = c.catalog.service('payhub')
if not services:
    raise Exception("No service found")

service = services[0]
service_address = f"http://{service['ServiceAddress']}:{service['ServicePort']}"

# 发送 HTTP 请求到 Kratos 服务
response = requests.get(f"{service_address}/your-endpoint")
print(response.status_code, response.text)
