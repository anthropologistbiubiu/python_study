import http.client
import urllib
import json



def post_demo():
   host = "localhost"
   port = "8080"
   conn = http.client.HTTPConnection(host,port)
   body = {"name":"sunweiming","age":18}
   url = "/api/data"
   # pararms = urllib.parse.urlencode({'number': 12524, '@type': 'issue', '@action': 'show'})
   json_data = json.dumps(body)
   headers = {"Content-Type": "application/json"}
   try:
        conn.request("POST", url, body=json_data, headers=headers)
        response = conn.getresponse()
        if response.status != 200:
            print(response.status)
            return
        data = response.read()
        print(data.decode('utf-8'))
   except IOError as e:
       print("IOError",e)
   except http.client.HTTPException as e:
       print("http.client.HTTPEXception",e)
   finally:
       print(conn.host)
       print(conn.port)
       conn.close()


if __name__ == '__main__':
    post_demo()