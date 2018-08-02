#!/usr/bin/python

number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    print 'success'
elif guess < number:
    print 'less than number'
else :
    print 'bigger than number'
