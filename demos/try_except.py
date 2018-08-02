#!/usr/bin/python

import sys

try:
	s = raw_input('Enter Somethine ---> ')
except EOFError:
	print '\nWhy did you do an EOF on me?'
	sys.exit()
except:
	print '\nSome error/exception occurred.'

print 'Done'
