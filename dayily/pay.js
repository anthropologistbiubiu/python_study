import http.client
import json

conn = http.client.HTTPSConnection("www.payhayu.com创建支付订单的入参callbackUrl")
payload = json.dumps({
   "orderNo": "1_359818241868632065",
   "merchantNo": "6097102022",
   "merTradeNo": "pm_2022110305",
   "amount": "150.00",
   "actualAmount": "150.00",
   "poundage": "4.00",
   "orderStatus": "1",
   "createTime": "1667455293000",
   "sign": "1DA4B890C7469CADECF7243817594111"
})
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}
conn.request("POST", "/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))