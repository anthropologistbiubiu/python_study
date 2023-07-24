import datetime




def main():
    current_time = datetime.datetime.now()
    print(current_time.strftime("%Y-%m-%d"))
    pass

if __name__ == '__main__':
    main()