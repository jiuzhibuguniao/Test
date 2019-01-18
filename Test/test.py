#scrapy爬虫框架
# from scrapy.spiders import Spider
#
#
# class BlogSpider(Spider):
#     name = 'woodenrobot'
#     start_urls = ['http://woodenrobot.me']
#
#     def parse(self, response):
#         titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
#         for title in titles:
#             print(title.strip())


# !/usr/bin/python
# -*- coding: UTF-8 -*-


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#正则表达式
# import re
# s = '1102231990xxxxxxxx'
# res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
# print(res.groupdict())


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#yield测试

# def test(data):
#     for row_data in data:
#         yield row_data
#
# if __name__=="__main__":
#     data=[1,2,3,4,5,6,7]
#     test_data=test(data)
#     print(list(test_data))


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#线程同步code


# import threading
# import time
# threadLock=threading.Lock()
#
#
# def print_time(ThreadName,delay,counter):
#     while counter:
#         time.sleep(delay)
#         print("%s,%s"%(ThreadName,time.ctime(time.time())))
#         counter-=1
#
#
# class myThread(threading.Thread):
#     def __init__(self,ID,NAME,COUNTER):
#         threading.Thread.__init__(self)
#         self.ID=ID
#         self.NAME=NAME
#         self.COUNTER=COUNTER
#
#     def run(self):
#         print("线程开始 ")
#         threadLock.acquire()
#         print_time(self.NAME,self.COUNTER,10)
#         threadLock.release()
#
#
#
# #创建线程池
# ThreadPool=[]
#
# #创建线程
# Thread1=myThread(1,"Thread-1",5)
# Thread2=myThread(2,"Thread-2",10)
#
# #开启新线程
# Thread1.start()
# Thread2.start()
#
# #补充线程池
# ThreadPool.append(Thread1)
# ThreadPool.append(Thread2)
#
#
# for row_thread in ThreadPool:
#     row_thread.join()
# print("完全结束！")


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#初步学习线程  _thread模块

# import _thread
# import time
#
# #创建函数
# def print_time(name,delay):
#     counter=0
#     while counter<10:
#         print("%s,%s"%(name,time.ctime(time.time())))
#         time.sleep(delay)
#         counter+=1
#
#
# #创建两个线程
# try:
#     _thread.start_new_thread(print_time,("Thread_1",5))
#     _thread.start_new_thread(print_time,("Thread_2",10))
# except:
#     print("That is over!")
#
# while 1:
#     pass


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#初步学习线程  threading 模块


# import threading
# import time
#
# exitFlag=0
#
# def print_time(ThreadName,delay,iteror):
#     while iteror:
#         if exitFlag:
#             ThreadName.exit()
#         time.sleep(delay)
#         print("%s,%s"%(ThreadName,time.ctime(time.time())))
#         iteror-=1
#
# class myThread(threading.Thread):
#     def __init__(self,ID,Name,delay):
#         threading.Thread.__init__(self)
#         self.ID=ID
#         self.Name=Name
#         self.delay=delay
#
#     def run(self):
#         print("线程开始"+self.Name)
#         print_time(self.Name,self.delay,10)
#         print("线程结束"+self.Name)
#
#
# #创建线程
# Thread_1=myThread(1,"Thread-1",5)
# Thread_2=myThread(2,"Thread-2",10)
#
# #开启线程
# Thread_1.start()
# Thread_2.start()
# Thread_1.join()
# Thread_2.join()
# print("主线程结束")




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#测试exit


# import threading
# import time
#
# exitFlag=0
#
# def print_time(ThreadName,delay,iteror):
#     while iteror:
#         if exitFlag:
#             ThreadName.exit()
#         time.sleep(delay)
#         print("%s,%s"%(ThreadName,time.ctime(time.time())))
#         iteror-=1
#
# class myThread(threading.Thread):
#     def __init__(self,ID,Name,delay):
#         threading.Thread.__init__(self)
#         self.ID=ID
#         self.Name=Name
#         self.delay=delay
#
#     def run(self):
#         print("线程开始"+self.Name)
#         print_time(self.Name,self.delay,10)
#         print("线程结束"+self.Name)
#
#
# #创建线程
# Thread_1=myThread(1,"Thread-1",5)
# Thread_2=myThread(2,"Thread-2",10)
#
# #开启线程
# Thread_1.start()
# Thread_2.start()
# Thread_1.join()
# Thread_2.join()
# print("主线程结束")



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#测试queue

# import queue
# import threading
# import time
#
# #初始化
#
# editFlag=0
#
#
#
#
#
#
#
# class myThread(threading.Thread):
#     def __init__(self,threadID,threadName,q):
#         threading.Thread.__init__(self)
#         self.threadID=threadID
#         self.threadName=threadName
#         self.q=q
#     def run(self):
#         print("进程开启： "+self.threadName)
#         proccessor(self.threadName,self.q)
#         print("进程结束： "+self.threadName)
#
#
# def proccessor(threadName,q):
#     while not editFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data=q.get()
#             queueLock.release()
#             print("%s,%s"%(threadName,data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
# threadName=['Thread-1','Thread-2','Thread-3']
# value=['one','two','three','four','five']
# queueLock=threading.Lock()
# workQueue=queue.Queue(10)
# threads=[]    #进程池
# threadID=1
#
# #填充值
#
#
# #初始化进程
# for row_threadName in threadName:
#     thread=myThread(threadID,row_threadName,workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID+=1
#
# queueLock.acquire()
# for row_value in value:
#     workQueue.put(row_value)
# queueLock.release()
#
# while not workQueue.empty():
#     pass
#
#
# editFlag=1
#
# for row_threads in threads:
#     row_threads.join()
#
#
# print("all is over!")


########################################################################################################################


# import queue
# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print ("开启线程：" + self.name)
#         process_data(self.name, self.q)
#         print ("退出线程：" + self.name)
#
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print ("%s processing %s" % (threadName, data))
#         else:
#             queueLock.release()
#         time.sleep(1)
#
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1
#
# # 创建新线程
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
#
# # 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
#
# # 等待队列清空
# while not workQueue.empty():
#     pass
#
# # 通知线程是时候退出
# exitFlag = 1
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#mysql-connector驱动

# import mysql.connector
#
# mysqldb=mysql.connector.connect(host="39.108.100.28",user="Rooobins",passwd="19910909kai",database='spiderData')
#
# mysqlcursor=mysqldb.cursor()
# mysqlcursor.execute("show tables;")
#
# # for x in mysqlcursor:
# #     print(x)
# #     print(type(x))
#
# print(mysqlcursor)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#测试pymysql



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 导入 socket、sys 模块
# import socket
# import sys
#
# # 创建 socket 对象
# serversocket = socket.socket(
#     socket.AF_INET, socket.SOCK_STREAM)
#
# # 获取本地主机名
# host = socket.gethostname()
#
# port = 9999
#
# # 绑定端口号
# serversocket.bind((host, port))
#
# # 设置最大连接数，超过后排队
# serversocket.listen(5)
#
# while True:
#     # 建立客户端连接
#     clientsocket, addr = serversocket.accept()
#
#     print("连接地址: %s" % str(addr))
#
#     msg = '欢迎访问菜鸟教程！' + "\r\n"
#     clientsocket.send(msg.encode('utf-8'))
#     clientsocket.close()

#***********************************************************************************************************************
# 导入 socket、sys 模块
# import socket
# import sys
#
# # 创建 socket 对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 获取本地主机名
# host = socket.gethostname()
#
# # 设置端口号
# port = 9999
#
# # 连接服务，指定主机和端口
# s.connect((host, port))
#
# # 接收小于 1024 字节的数据
# msg = s.recv(1024)
#
# s.close()
#
# print (msg.decode('utf-8'))

#***********************************************************************************************************************
# import sys
# import socket
#
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn',80))
# s.send(bytes('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n','utf-8'))
#
# #接收数据
# buffer=[]
# while True:
#     #每次最多接收1K数据
#     d=s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# buffer_1=[str(i) for i in buffer]
#
# data=''.join(buffer_1)
#
# #关闭连接
# s.close()
#
# header,html=data.split('\\r\\n\\r\\n')
# print(header)
#
# #把接收到的数据写入文件
# with open("./Data/sina.html",'w+') as f:
#     f.write(html)
#***********************************************************************************************************************
#服务器

# import sys
# import socket
# import threading
# import time
#
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定窗口
# s.bind(('127.0.0.1',9999))
# s.listen(5)
#
# print('waiting for connection...')
#
# def tcplink(sock,addr):
#     print("Accept new connection from %s:%s..."%(addr))
#     sock.send(bytes("Welcome!",'utf-8'))
#     while True:
#         data=sock.recv(1024)
#         time.sleep(1)
#         if (data=='exit') or (not data):
#             break
#         sock.send(bytes(data))
#         sock.close()
#         print("Connection from %s:%s closed."%(addr))
#
# while True:
#     #接受一个新连接
#     sock,addr=s.accept()
#     #创建新线程来处理TCP连接：
#     t=threading.Thread(target=tcplink,args=(sock,addr))
#     t.start()


#***********************************************************************************************************************
#客户端
# import sys
# import socket
#
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# s.connect(('127.0.0.1',9999))
# print(s.recv(1024))
#
# for data in ["wangkai","wangzhen",'zhengyang','fenyang']:
#     s.send(bytes(data))
#     print(s.recv(1024))
#
# s.send(bytes('exit'))
# s.close()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#subprocessing测试
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#测试os
# import os
#
# print("%s got start..."%(os.getpid()))
# pid=os.fork()
#
# if pid==0:
#     print("i am %s,and My parent is %s."%(os.getpid(),os.getppid()))
# else:
#     print("i am child %s,and my parent is %s."%(pid,os.getpid()))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#multiprocessing测试Process
# from multiprocessing import Process
# import os
# import sys
#
# def process_test(name):
#     print("the child task %s %s start."%(name,os.getpid()))
#
#
# if __name__=="__main__":
#     print("Three!Two!One! parent %s start..."%(os.getpid()))
#     p=Process(target=process_test,args=("TEST",))
#     print("The child pid will start.")
#     p.start()
#     p.join()
#     print("all is over.")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#multiprocesssing测试pool
# from multiprocessing import Pool
# import os
# import time
# import random
#
#
# def test(name):
#     print("The childent task %s %s get start..."%(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print("The childent task %s %s cost %s times."%(name,os.getpid(),end-start))
#
# if __name__=="__main__":
#     print("The parent task %s get start..."%(os.getpid()))
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(test,(i,))
#     print("subprocess get start...")
#     p.close()
#     p.join()
#     print("ALL IS OVER.")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import subprocess
#
# print("$ nslookup www.python.org")
# r=subprocess.call(['nslookup','www.python.org'])
# print('exit code. ',r)
#***********************************************************************************************************************
# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('GBK'))
# print('Exit code:', p.returncode)
#***********************************************************************************************************************
# from multiprocessing import Queue,Process
# import random,os,time
#
# def write(q):
#     print("Queue for write: %s..."%(os.getpid()))
#     for value in ["wangkai",'wangzhen','zhengyang','fenyang']:
#         print("value %s write in Queue"%(value))
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     print("Queue for read: %s..."%(os.getpid()))
#     while True:
#         data=q.get()
#         print("value %s read from Queue."%(data))
#
# if __name__=="__main__":
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
# 
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
# 
# c = consumer()
# produce(c)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import os
# print(os.path.abspath("."))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import os
# # ls=[x for x in os.listdir('.') if os.path.isdir(x)]
# # for data in ls:
# #     print(data)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#杨辉三角
# def triangles(max):
#     a,b=[1],[1,1]
#     n=3
#     yield a
#     yield b
#     while n<max:
#         c=[]
#         c.append(1)
#         for data in range(2,n):
#             c.append(b[data-2]+b[data-1])
#         c.append(1)
#         n=n+1
#         b=c
#         yield b
#     return "done"
#
#
#
# generator_triangles=triangles(10)
# while True:
#     try:
#         x=next(generator_triangles)
#         print("generator_triangles: ",x)
#     except StopIteration as e:
#         print("Generator return value: ",e.value)
#         break
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# generator_test=(x for x in range(10))
# while True:
#     try:
#         g=next(generator_test)
#         print(g)
#     except StopIteration as e:
#         print(e.value)
#         break
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def test(x):
#     return x*x
# lls_1=[1,2,3,4,5,6,7,8,9]
# lls_2=map(test,lls_1)
# print(list(lls_2))
#*****************************************************************************************************
# from collections import Iterable,Iterator
# from functools import reduce
#
# def add(x,y):
#     return x+y
#
# def fn(x,y):
#     return x*10+y
#
# lls_1=[1,2,3,4,5,6,7,8,9,10]
#
# DIGSTS={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
#
# def str2num(s):
#     def fn(x,y):
#         return x*10+y
#     def str2list(z):
#         return DIGSTS[z]
#     return reduce(lambda x,y:x*10+y,map(str2list,s))
# print(str2num("1359"))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def is_odd(n):
#     return n%2==1
#
# def not_empty(s):
#     return s.strip(" ") and s
#
# lls_1=filter(is_odd,[1,2,3,4,5,6,7,8,9])
# lls_2=filter(not_empty,["A","B  ","   ","  c"])
# print(list(lls_2))
#****************************************************************************************************************

# def _odd_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n
#
# def _not_divisible(n):
#     return lambda x:x%n>0
#
#
# def primes():
#     yield 2
#     it=_odd_iter()
#     while True:
#         n=next(it)
#         yield n
#         it=filter(_not_divisible(n),it)
#
# for data in primes():
#     if data<100:
#         print(data)
#     else:
#         break

#***********************************************************************************************************************
# import math
#
# def number():
#     n=0
#     yield 0
#     while True:
#         n=n+1
#         yield n
#
#
# def select_number(n):
#     N=str(n)
#     s=1
#     for i in range(math.ceil(len(N)/2)):
#         if N[i]==N[len(N)-1-i]:
#             s=(s and 1)
#         else:
#             s=(s and 0)
#     if s:
#         return n
#     # else:
#     #     return
#
# all_number_select=filter(select_number,number())
#
# # print(list(all_number_select))
#
# for i in all_number_select:
#     if i<=200:
#         print(i)
#     else:
#         break
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L_test=[]
#
# for i in L:
#     L_test.append(i[0])
#
# L_test_1=sorted(L_test)
# index=[]
# for data_L_test_1 in L_test_1:
#     index.append(L_test.index(data_L_test_1))
#
# end=[]
# for row_index in index:
#     end.append(L[row_index])
#
# print(end)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def person_1(*args):
#     sum=0
#     for data in args:
#         sum=data+sum
#     return sum
#
# lls_1=[1,2,3,4,5,6,7,8,9,10]
# lls_2=(1,2,3,4,5,6,7,8,9,10)
#
# print(person_1(*lls_1))
# print(person_1(*lls_2))

# def person_2(name,gender,**kwargs):
#     return {"name":name,"gender":gender,"others":kwargs}
#
# print(person_2("wangkai",'male',city="taiyuan"))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def sum_test(*args):
#     def test():
#         sum=0
#         for data in args:
#             sum=data+sum
#         return sum
#     return test
#
# lls_1=[1,2,3,4,5,6,7,8,9,10]
# f=sum_test(*lls_1)
# print(f)
# print(type(f))
# print(f())
#***********************************************************************************************************************

# def test(*args):
#     fs=[]
#     for i in args:
#         def test_1():
#             return i*i
#         fs.append(test_1)
#     return fs
#
# lls_1=[1,2,3]
#
# lls=test(*lls_1)
# print(lls[0](),lls[1](),lls[2]())

#***********************************************************************************************************************

# def test(*args):
#     js=[]
#     def sum_test(j):
#         def test_1():
#             return j*j
#         return test_1
#     for data in args:
#         js.append(sum_test(data))
#     return js
#
# lls_1=[1,2,3]
# print(test(*lls_1)[2]())

#***********************************************************************************************************************
# lls=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==1,lls)))
#***********************************************************************************************************************

# def log(func):
#     def wrapper(*args,**kwargs):
#         print("%s function was called."%(func.__name__))
#         return func(*args,**kwargs)
#     return wrapper
#
# @log
# def now():
#     print("This is a Test.")
#
# print(now.__name__)

# import requests
# header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
# url="http://www.zhihu.com"
# text=requests.get(url,headers=header)
# print(text)

#***********************************************************************************************************************
# print("hello world")

#消费者系统
def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print(n)
        print('[CONSUMER] Consuming %s...'%(n))
        r='200 OK'

#生产者系统
def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[PRODUCER] Producing %s...'%(n))
        r=c.send(n)
        print('[PRODUCER] Consumer return: %s'%(r))
    c.close()






if __name__=="__main__":
    c=consumer()
    produce(c)