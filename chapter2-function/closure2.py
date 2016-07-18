'''
闭包在python中通过函数调用创建。
在这个例子中，每次调用makeInc，创建一个新的Inc函数实例。
但是，每个实例链接的不同的x值.

这个例子展示了使用闭包消除硬编码的常量和全局变量。
'''
def makeInc(x):
	def inc(y):
		# x is "closed" in the definition of inc
		return y + x
	return inc

inc5 = makeInc(5) 
print(inc5) #<function makeInc.<locals>.inc at 0x01CC6228>

inc10 = makeInc(10)
print(inc10) #<function makeInc.<locals>.inc at 0x01CC6270>

print(inc5(5)) #10

print(inc10(5)) #15


import time
keepRunning = True
updates = []

def runLoop():
	
	for u in updates:
		u()
'''
在Python中，所有的方法(不是函数) 在某种程度上都属于闭包。
foo.update包住了类foo.
g.update是一个储存了值g的闭包函数。
'''
class foo():
	def __init__(self, x = 0):
		self.x = x

	def update(self):
		print(self.x)
		self.x += 1

f = foo()
g = foo(2)

updates.extend([f.update, g.update])

runLoop()


