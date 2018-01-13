import threading


def thread_job():
    print(threading.active_count())
    #查看所有的线程
    print(threading.enumerate())

    #查看现在正在运行的线程
    print(threading.current_thread())

    print("This is a thread of %s"%threading.current_thread())

def main():
    #添加线程
    thread = threading.Thread(target = thread_job,)
    thread.start()

    print(threading.active_count())

    #查看所有的线程
    print(threading.enumerate())

    #查看现在正在运行的线程
    print(threading.current_thread())

if __name__ =="__main__":
    main()
