class A(object):
	pass

def hello(self):
	print("hello..")

a = A()
a.hello = hello

#hello() missing 1 required positional argument: 'self'
#a.hello()

print(a.hello) #<function hello at ..>
a.hello(1) 

class B(object):
	def b_hello(self):
		print("hello") 

print(B.b_hello) #<function B.b_hello at ...>
'''我们注意观察上面的a.hello和B.b_hello信息的不同
	正常情况下,类的方法前面会有所属的类的信息,如B.b_hello
'''
print(B().b_hello)