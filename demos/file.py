#!/usr/bin/python

f = open('poem.txt','r')

print f.read(2)
print f.readline(2)
print f.readlines()


with open('poem.txt','r') as fh:
	for line in fh:
		print line,


with file('poem.txt') as f1:
	data = f1.readlines()

for line in data:
	words = line.split()
	print words
