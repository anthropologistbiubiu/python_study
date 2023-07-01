from queue import Queue
import random, threading, time


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue,lock):
        threading.Thread.__init__(self, name=name)
        self.queue = queue
        self.lock = lock
    def run(self):
        for i in range(1, 5):
            print(" %d is producing {} to the queue!" % i)
            self.queue.put(i)
        # print("%s finished!" % self.getName())


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue,lock):
        threading.Thread.__init__(self, name=name)
        self.lock = lock
        self.queue = queue

    def run(self):
        if self.queue.empty():
            return
        else:
            for i in range(1, 5):
                val = self.queue.get()
                print("{} is consuming {} in the queue.".format(val,i))
            # print("%s finished!" % self.getName())


def main():
    queue = Queue()
    lock = threading.Lock()
    producer = Producer('Producer', queue,lock)
    consumer = Consumer('Consumer', queue,lock)

    producer.start()
    time.sleep(5)
    consumer.start()

    producer.join()
    consumer.join()
    print('All threads finished!')


if __name__ == '__main__':
    main()