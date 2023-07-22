
import json



def main():
   pass


def obj_To_Json():
    json_str = '{"name": "John Doe", "age": 30, "is_student": true}'
    # 将JSON字符串解析为Python字典
    json_dict = json.loads(json_str)

    # 输出Python字典
    print(json_dict)

    # 输出字典中的值
    print(json_dict['name'])
    print(json_dict['age'])
    print(json_dict['is_student'])
    pass
def json_To_Dict():
    person_dict = {'name': 'John Doe', 'age': 30, 'is_student': True}

    # 将Python字典转换为JSON字符串
    json_str = json.dumps(person_dict)
    print(json_str)
    pass
# 处理JSON数组
def json_To_List():
    json_arr = '["apple", "banana", "orange"]'

    # 将JSON数组解析为Python列表
    py_list = json.loads(json_arr)

    # 输出Python列表
    print(py_list)
    print(type(py_list))
def list_To_Json():
    # Python列表
    py_list = ["apple", "banana", "orange"]
    # 将Python列表转换为JSON数组
    json_arr = json.dumps(py_list)
    # 输出JSON数组
    print(json_arr)
    print(type(json_arr))
def tuple_to_json():

    tup = ("Dhirubhai", 72, True, 5.8)
    jsonObj = json.dumps(tup)
    print(jsonObj)
    print(type(jsonObj))
def json_to_tuple():
    jsonTup = '{"Dhirubhai", 72, true, 5.8}'
    tup = json.loads(jsonTup) # 元组字符串不能直接序列化为内置对象
    print(tup)
    print(type(tup))

if __name__ == '__main__':
    tuple_to_json()