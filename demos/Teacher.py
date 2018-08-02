#!/usr/bin/python


class SchoolMember:
	def __init__(self,name,age):
        	self.name = name
        	self.age = age


	def tell(self):
        	print 'Name:%s,age:%s' % (self.name,self.age)

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print '(Initialized Teacher: %s)' % self.name
	
	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: "%d"' % self.salary


t = Teacher('Mrs. Shrividya', 40, 30000)

for t in (t,t):
	t.tell()
