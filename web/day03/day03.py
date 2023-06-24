import http.client
import json

# conn = http.client.HTTPSConnection("")

reqData = {"amount":500,"code":200,"createTimeL":""}
postData = json.dumps(reqData)
print("postData: ",postData)
payload = json.dumps({
   "amount": "5000",
   "code": 200,
   "createTimeL": 1680334544698,
   "endToEndId": "e00360305202304010736c2009ae8cdd",
   "fee": "150",
   "merchantOrderId": "164774677175285280-6-WVDVe",
   "msg": "PAID",
   "orderId": "S110202304011642068212621467648",
   "payType": "110",
   "payUrl": "https://pay2.mtbtop1.com/s3/checkout-page/v3.html?cid=expireAt%202023-04-01T05:35:44.725466&sid=S110202304011642068212621467648&amount=50&qrcode=00020101021226790014br.gov.bcb.pix2557brcode.starkinfra.com/v2/92cde06bbe9e4a15a349756d2d24a6325204000053039865802BR5925Wudi%20pay%20Correspondente%20d6009Sao%20Paulo62070503***63045AE8",
   "realPayAmount": "5000",
   "sign": "674e8a79f04939a44fda447d4b13ca8c",
   "status": "01",
   "traceId": "i200,i200401ec75e3c58a5a40cdb874d30bedabcb5c"
})
print(payload)
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}
"""
conn.request("POST", "/notifyUrl", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
"""