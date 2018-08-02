#!/usr/bin/python


def fun1(a, b=5, c=10) :
	print 'a = ' ,a,'b = ',b,'c = ',c

fun1(2);
fun1(2,3)
fun1(2,c=5)
fun1(c=3,a=2)
