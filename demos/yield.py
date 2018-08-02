#! /usr/bin/python

import sys

def fibonacci(n):
	a=0
	b=1
	counter=0
	while True:
		if(counter > n):
			return
		yield a
		a=b
		b=a+b
		counter += 1
n = int(raw_input("enter the loop number:"))
f = fibonacci(n)
index = 0
while index < n:
	try:
		print (next(f))
		index += 1
	except StopIteration:
		sys.exit()

