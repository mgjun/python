#!/usr/bin/pyhon

number = 23;
running = True;

while running :
	guess = int(raw_input('Enter an integer : '));
	if guess == number:
		print 'success';
		running = False;
	elif guess < number:
		print 'less than number';
	else :
		print 'bigger than number';
else :
	print 'end loop'
