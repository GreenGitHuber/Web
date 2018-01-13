import threading
import time

def T1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1) # 任务间隔0.1s
    print("T1 finish\n")

def T2_job():
    print("T2 start\n")
    # for i in range(30):
    #     time.sleep(0.1) # 任务间隔0.1s
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')
thread_2 = threading.Thread(target=T2_job, name='T2')
# thread_1.start() # 开启T1
# thread_1.join()
# thread_2.start()
# thread_2.join()
# print("all done\n")
'''
T1 start
T1 finish
T2 start
T2 finish
all done
'''
# thread_1.start() # 开启T1
# thread_2.start()
# thread_2.join()
# thread_1.join()
# print("all done\n")
'''
T1 start
T2 start
T2 finish
T1 finish
all done
'''
# thread_1.start() # 开启T1
# thread_2.start()
# thread_1.join()
# thread_2.join()
# print("all done\n")
'''
T1 start
T2 start
T2 finish
T1 finish
all done
'''
thread_1.start() # 开启T1
thread_2.start()
thread_2.join()
thread_1.join()
print("all done\n")
'''
T1 start

T2 start

T1 finish

T2 finish

all done
'''
