import _thread
import time


# 为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#
#
# # 创建两个线程
# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 2,))
#     _thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print("Error: unable to start thread")
#
# while 1:
#     pass



def loop1():
    count=0
    while count<5:
        time.sleep(3)
        print("loop1: ",time.ctime())

def loop2():
    count=0
    while count<5:
        time.sleep(3)
        print("loop2: ",time.ctime())


#创建两个进程
try:
    _thread.start_new_thread(loop1,())
    _thread.start_new_thread(loop2,())
except:
    print("Error: please try a again.")



while 1:
    pass
