import json

print(json.__all__)
# json 对象序列化
info = {"name":"sunweiming","age":18}
json_info = json.dumps(info)
print(json_info)
print("json_info",type(json_info))

stu = json.loads(json_info)
print("stu ",stu)
print("stu type",type(stu))

# json 数组序列化
data = [{
    "id": 1,
    "name": "test1",
    "age": "1"
}, {
    "id": 2,
    "name": "test2",
    "age": "2"
}]

json_data = json.dumps(data)
print(json_data)



