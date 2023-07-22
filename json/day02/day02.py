
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

    pass
if __name__ == '__main__':
    obj_To_Json()