#! /usr/bin/python3

import threading
import time

class MyThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ("start thread:" + self.name)
		threadLock.acquire()
		print_time(self.name,self.counter,self.counter)
		threadLock.release()



def print_time(threadName,delay,counter):
	while counter > 0:
		time.sleep(delay)
		counter -= 1
		print ("%s:%s" % (threadName,time.ctime(time.time())))

threadLock = threading.Lock()
threads = []

t1 = MyThread(1,"Thread-1",1)
t2 = MyThread(2,"Thread-2",2)

t1.start()
t2.start()

threads.append(t1)
threads.append(t2)

for t in threads:
	t.join()
print("exit main thread")

