'''
协程：

子程序，又称为函数，在所有语言中都是层级调用。
		比如，A调用B,B在执行过程中又调用了C,
		C执行完毕后返回,B执行完毕后返回,最后A执行完毕.

在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
这种情况称为函数间的调用。

协程本质上也是一种子程序，或者说，子程序也是一种协程。
不同的是，普通的子程序无法实现两个函数间的多次相互调用。
	注：把函数看成对象。
		这里所说的调用是针对特定的一个函数对象，当我们通过函数名称多次调用一个函数时，其实创建了多个函数。
也就是说，我们无法交替中断两个函数。

实际上，协程就是类函数一样的程序组件。
只不过子例程只有一个调用入口起始点，返回之后就结束了。
而协程入口既可以是起始点，又可以从上一个返回点继续执行。


协作式多任务，而非传统的抢占式。并且，我们可以说，子程序就是协程的一种特例。
协作式多任务的优点在于不需要对共享状态进行加锁维护，由于是自己主动让出CUP执行权，所以只需判断状态即可保证安全性。	
并且更加轻量级。
'''

#consumer是一个generator.
def consumer():
	r = ""
	while True:
		n = yield r
		if not n:
			return
		print("[CONSUMER] Consuming %s" % n)
		r = '200 ok'

def produce(c):
	c.send(None) #启动生成器。
	r = 0
	while r < 5:
		r += 1
		print('[PRODUCER] Producing %s' % r)
		re = c.send(r) #一旦产生了东西，通过c.send(r)切换回consumer。
		print('Consumer return： %s' % re)
	c.close()	

c = consumer() #<generator object consumer at 0x01A60630>
print(c)
produce(c)


#使用对象来模拟协程。本质是两个对象间的多次相互调用。
class consumer(object):
	def __init__(self):
		self.n = ""

	def consumer(self, r):
		print("CONSUMER %s" % r)
		self.n = '200 ok'
		return self.n

class produce(object):
	def __init__(self, c):
		self.r = 0
		self.c = c
	
	def produce(self):
		while self.r < 5:
			self.r += 1
			print("[PRODUCES] %s " % self.r)
			result = c.consumer(self.r)
			print("CONSUMER　RETURN %s" % result)

print("==================")
c = consumer()
produce(c).produce()