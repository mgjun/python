#! /usr/bin/python3


import json

filename = 'username.json'

try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name?")
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	print ('user :' + username+ 'has save to json file')
else:
	print ("Welcome back ," + username + "!")
