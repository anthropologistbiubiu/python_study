# 原生网络库的学习
import requests

# 发送get 请求
def get_available_amount():
    get_url = 'http://api.spxysz.com/pay/getPartner?partnerId=1000100020003271&sign=CF75DFF76E56812EA3C5B49C60E1C389&type=default&version=1.0'
    response = requests.get(get_url)
    print(response.text)


# 发送带参数的get 请求
def get_req_with_params():
    get_url = 'http://api.spxysz.com/pay/getPartner'
    params = {"partnerId":"1000100020003271","sign":"CF75DFF76E56812EA3C5B49C60E1C389","type":"default","version":"1.0"}
    response = requests.get(get_url,params=params)
    print(response.text)

# 3. 发送 POST 请求
def post_req():
    post_url = 'https://queryapi.metagopayments.com/cashier/balance.ac'
    form_data = {""}
    response = requests.post(url=post_url)
    print(response.text)

def post_json_req():
    pass
def main():
    post_req()
if __name__ == '__main__':
    main()
