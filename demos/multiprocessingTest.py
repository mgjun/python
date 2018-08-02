#! /usr/bin/python
#coding=utf-8

from multiprocessing import Pool
from threading import Thread

from multiprocessing import Process
import time

def loop(threadIndex):
	counter,delay = 3,1
	while counter > 0:
		time.sleep(delay)
		print ("start process "+str((threadIndex)))
		counter -= 1

if __name__ == '__main__':
	threads = []
	for i in range(3):
		t = Process(target=loop,args=(i,))
		t.start()
		threads.append(t)
	for t in threads:
		t.join()
	print ("exit main thread")
