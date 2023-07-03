import json

list = ['Apple', 'Huawei', 'selenium', 'java', 'python']
# 把list先序列化，写入到一个文件中
# 两步操作 1步先序列化 列表对象  2步把序列化成的字符串写入文件
json.dump(list, open('./test.txt', 'w'))
r1 = open('./test.txt', 'r')
print(r1.read())
# ["Apple", "Huawei", "selenium", "java", "python"]


content = json.load(open("./test.txt", "r"))
print("content",content)
print("content type",type(content))
