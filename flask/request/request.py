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
    form_data = {"account":"230803000026810232","custId":"23080300002681","orgNo":"8230801142","sign":"96d644376b0c9b22e1b25f023828cd55","version":"2.1"}
    response = requests.post(url=post_url,data=form_data,headers={'Content-type':'application/x-www-form-urlencoded'})
    print(response.text)

def post_json_req():
    post_url = 'http://api.stimulatepay.com/account/payout/balance'
    json_data = {"merchantId":"i2BByFRIxHrGhpA1","sign":"d1a15e2068a78f6890e0eff80903e08f"}
    response = requests.post(post_url,json=json_data,headers={'Content-Type':'application/json'})
    print(response.text)

def main():
    post_json_req()
if __name__ == '__main__':
    main()
