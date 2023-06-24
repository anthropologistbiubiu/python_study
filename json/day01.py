import json

print(json.__all__)

info = {"name":"sunweiming","age":18}
json_info = json.dumps(info)
print(json_info)
print("json_info",type(json_info))

stu = json.loads(json_info)
print("stu ",stu)
print("stu type",type(stu))
