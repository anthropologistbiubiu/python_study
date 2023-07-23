import requests


def file_upload():
    url = "http://127.0.0.1:8080/file/upload"
    files = {'file': open('myfile.txt', 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print(response)
        print("文件上传成功！")
    else:
        print("文件上传失败，状态码：", response.status_code)


if __name__ == '__main__':
    file_upload()