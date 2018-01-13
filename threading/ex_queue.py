#使用Queue存储线程结果

import threading
from queue import Queue 

def job(l,q):
    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)


def multithread():
    q = Queue()
    threads = []
    res = []
    data = [[1,2,3],[2,3,4],[4,5,6]]
    for i in range(len(data)):
        thread = threading.Thread(target = job,args=(data[i],q))
        threads.append(thread)
    for thread in threads:
        thread.start()
        thread.join()
    for _ in range(len(data)):
        res.append(q.get())
    print(res)

if __name__ == '__main__':
    multithread()
