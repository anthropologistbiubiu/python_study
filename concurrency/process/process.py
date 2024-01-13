
import multiprocessing
import time
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

def data_ready(event):
    print('我已经开始准备数据了')
    time.sleep(2)
    print('数据准备完成')
    event.set()

def data_process(event):
    print('我已经准备开始消费数据了')
    event.wait()
    time.sleep(5)
    print('数据消费完成')



# 进程之间通过pipe 来实现数据通信
def pipe_data_ready(pipe):
    print('pipe_data_ready')
    count = 1
    while count < 10:
        print(count)
        pipe.send(count)
        count += 1
    pipe.send(None)
    pipe.close()

def pipe_data_consumer(pipe):

    while True:
        message =  pipe.recv()
        if message == None:
            break
        print(f'pipe_data_consumer {message}')
    print('pipe_data_consumer finish')
    pipe.close()
    return



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

    event = multiprocessing.Event()
    producer = multiprocessing.Process(target=data_ready,args=(event,))
    consumer = multiprocessing.Process(target=data_process,args=(event,))

    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    producer_pipe,consumer_pipe =  multiprocessing.Pipe()

    pipe_producer = multiprocessing.Process(target=pipe_data_ready,args=(consumer_pipe,))
    pipe_consumer = multiprocessing.Process(target=pipe_data_consumer,args=(producer_pipe,))

    pipe_producer.start()
    pipe_consumer.start()
    pipe_producer.join()
    pipe_consumer.join()


if __name__ == '__main__':
    main()



