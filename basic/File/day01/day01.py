

# 只读（“r”）：这种模式以只读模式打开文本文件。文件的开始是句柄所在的位置。如果文件不存在，它将引发 I/O 错误。这也是打开文件的默认模式。
# 读和写（'r+’）：这种方法以读和写模式打开文件。文件的开始是句柄所在的位置。如果文件不存在，就会产生一个 I/O 错误。

def r_open():
    f = open("myfile.txt", "x")
    file_name = f.name()
    print(file_name)

if __name__ == '__main__':
    r_open()