results = [];
def loopdict(dictObj):
	for key,value in dictObj.items():
		if isinstance(value,str):
			results.append(key + "--" + value)
		elif isinstance(value,dict):
			loopdict(value)	

users = {
	"username":"test",
	"firstname":"m",
	"lastname":{
		"name":"1",
		"user":"mickey"
	}
}
loopdict(users)
if results:
	for result in results:
		print (result)
