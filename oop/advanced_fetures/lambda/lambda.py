


# 总结lambda 表达式的用法

# 基本形式
add = lambda x,y: x+y
print(add(1,2))

# 与内置函数的一起使用
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2,numbers))
print(squares)

evens = list(filter(lambda x: x % 2 == 0,numbers))
print(evens)

dict = [(1,'sun'),(3,'wei'),(2,'ming')]
sorted_dict = sorted(dict,key=lambda x : dict[0])
print(sorted_dict)

# 作为参数传递给其他函数


def operator(x,y,func):
    return func(x,y)




if __name__ == '__main__':
    print(operator(1,2,add))












