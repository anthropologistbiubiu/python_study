# 选择语句
grade = float(input())
if grade <60:
    print("不及格")
elif grade  < 85:
    print("良好")
else:
    print("优秀")

# 循环语句1
print('循环语句1')
for item in ['sun','wei','ming']:
    print(item)
# 循环语句2
print('循环语句2')
for item in range (1,5,2):
    print(item)

# 循环语句3
print('循环语句3')
i = 0
while i < 5:
    i+=1
    print(i)


# 循环语句4
print('循环语句4')
for item in ('a','b',9):
    print(item)

# 字符串循环
print('字符串循环')
for item in "12345":
    print(item)

# break continue 语句


# 元组循环

# 列表和元组的使用特点
# 可变性：
# 列表是可变的（Mutable）：你可以修改、添加和删除列表中的元素。
# 元组是不可变的（Immutable）：一旦创建，元组的元素不能被修改、添加或删除。

# 相同点：
# 有序性：列表和元组都是有序的，即其中的元素按照特定的顺序排列。
# 可迭代性：你可以使用循环（例如for循环）遍历列表和元组中的元素。
# 支持索引和切片：你可以使用索引访问列表和元组中的元素，并且可以使用切片操作获取部分元素。



# list操作

# insert 操作
mylist = ['a','b','c']
print(mylist.insert(1,'d'),mylist)
# append 操作
print(mylist.append('e'),mylist)
# extend 操作
print(mylist.extend('f'),mylist)











