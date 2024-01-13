
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

# 进程的创建和使用
def my_process(i):
    print(f'{i} my_process')

# 进程池

def my_process_pool(i):
    print('my_process_pool')
    return i**2



# 共享变量


def my_function(shared_variable, lock, i):
    with lock:
        shared_variable.value += i



# 进程的事件通知


def main():

    process1 = multiprocessing.Process(target=my_process, args=(10,))
    process1.start()
    process1.join()

    with ProcessPoolExecutor(max_workers=10) as executor:
        for i in range(10):
            future = executor.submit(my_process_pool,i)
            print(future.result())


    shared_variable  = multiprocessing.Value('i',0)
    lock = multiprocessing.Lock()

    process_list = [multiprocessing.Process(target=my_function,args=(shared_variable,lock,i,)) for i in range (10)]
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    print(shared_variable.value)





if __name__ == '__main__':
    main()



