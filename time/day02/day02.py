import datetime
import time


def main():
    current_time = datetime.datetime.now()
    print(current_time.strftime("%Y-%m-%d"))
    timestamp = time.time()
    print(timestamp)
    utc_time = datetime.datetime.utcfromtimestamp(timestamp)
    print(utc_time)
    pass

if __name__ == '__main__':
    main()