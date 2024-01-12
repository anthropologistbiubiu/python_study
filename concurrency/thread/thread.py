import threading
import random
import time
import queue
from concurrent.futures import ThreadPoolExecutor


# 创建和使用线程
def my_task():
    print(f'my_task start')


thread = threading.Thread(target=my_task)
thread.start()
thread.join()
print('--------------------------------')
# 多线程并发控制
my_list = []
lock = threading.Lock()


def my_task_control(i):
    print(f'my_task_control {i} start')
    time.sleep(1)
    global my_list
    with lock:
        random_num = random.randint(1, 100)
        my_list.append(random_num)


threads = [threading.Thread(target=my_task_control, args=(i,)) for i in range(10)]
for thread in threads:
    thread.start()
print('please wait for litte time')
for thread in threads:
    thread.join()
print(my_list)
print('-----------------------------')
# 多线程之间的通信 使用queue来安全传递消息,这个就类似于golang中的管道
my_queue = queue.Queue()


def my_task_queue(my_queue, i):
    print(f'my_task_queue {i} start')
    time.sleep(1)
    random_num = random.randint(1, 100)
    my_queue.put(random_num)


def my_consumer_func(my_queue):
    print(my_queue.get())


threads = [threading.Thread(target=my_task_queue, args=(my_queue, i,)) for i in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

threads = [threading.Thread(target=my_consumer_func, args=(my_queue,)) for i in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
# 线程池 提高线程的复用率,减少开销,类似于golang 的协程池
print('---------------------------------')
my_pool_queue = queue.Queue()


def my_pool(i):
    time.sleep(1)
    print(f'the {i} worker start work')
    my_pool_queue.put(i ** 2)


with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(10):
        future = executor.submit(my_pool, i)
my_pool_queue.put(None)
while my_pool_queue:
    item = my_pool_queue.get()
    if item == None:
        break
    print(item)

# 5. 使用 threading.Event 实现线程间通信：

print('--------------------------------------')


def my_trigger(event):
    print(f'I am starting to prepare the data.')
    time.sleep(2)
    print(f'I am ready with the data')
    event.set()


def data_process(event):
    print(f'I am ready to process the data.')
    event.wait()
    time.sleep(1)
    print(f'I have finished processing the data.')


trigger = threading.Event()

trigger_thread = threading.Thread(target=my_trigger, args=(trigger,))

data_process_thread = threading.Thread(target=data_process, args=(trigger,))

trigger_thread.start()
data_process_thread.start()

trigger_thread.join()
trigger_thread.join()


# 6. 使用 threading.Timer 定时执行任务：
def my_timer():
    print(f'starrt my_timer task')
    pass


timer = threading.Timer(5, my_timer)
timer.start()
# timer.cancel()







