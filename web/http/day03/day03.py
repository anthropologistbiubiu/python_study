# x-www-form-urlencode
import http.client
import urllib.parse


def send_urlencode_form_data():
    host = "127.0.0.1"
    port = "8080"
    path = "/submit/x-www-form-urlencode"
    conn = http.client.HTTPConnection(host=host,port=port)
    params = {"name":"sunweiming","email":"1318947957@qq.com","message":"ok"}
    body = urllib.parse.urlencode(params)
    print(body)
    headers = {"Content-Type":"x-www-form-urlencoded"}
    try:
        conn.request("POST", path, body=body , headers=headers)
        response = conn.getresponse()
        if response.status != 200:
           print(response.status)
        else:
            data = response.read()
            print(data.decode('utf-8'))
    except IOError as e:
        print("IOError",e)
    except http.client.HTTPException as e:
        print("HTTPException ",e)
    finally:
        print(conn.host)







if __name__ == '__main__':
    send_urlencode_form_data()