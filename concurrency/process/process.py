

import multiprocessing
from concurrent.futures import ProcessPoolExecutor

# 进程的创建和使用

def my_process(i):
    print(f'{i} my_process')

# 进程池

def my_process_pool(i):
    print('my_process_pool')
    return i**2



def main():
    process1 = multiprocessing.Process(target=my_process, args=(10,))
    process1.start()
    process1.join()

    with ProcessPoolExecutor(max_workers=10) as executor:
        for i in range(10):
            future = executor.submit(my_process_pool,i)
            print(future.result())


if __name__ == '__main__':
    main()



