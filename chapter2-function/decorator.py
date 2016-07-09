'''装饰器.
	从技术上讲,Python装饰器是通过闭包来实现的.
	一个装饰器方法接收一个被增强的函数,返回一个
	增强了的函数.
'''

#因为log要为一个decorator,所以接受一个函数
#作为参数,并返回一个函数.
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2016-06-19')

now()

'''
	上面通过@decorator语法对log方法对now函数进行了增强.
	相当于执行了now = log(now).下面是示例代码.

	当调用log时,传入要增强的函数,返回一个wrapper函数.
	所以,当我们再次调用传入的函数时,其实我们调用的是wrapper.
	也就是说原先的函数变量名已经指向了wrapper函数对象.
	 
'''

def now2(time):
	print('now2: %s' % time)

now2 = log(now2)
now2('2016-06-19')

'''decorator本身需要参数.
	
'''
def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print("%s %s():" % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log2('execute')
def now3():
	print('2016-06-20')

def now4(time):
	print('now 4:%s' % time )
now3() #execute now3():
	   #2016-06-20
#等效于:
print('---')
decorator = log2('execute') 
wrapper = decorator(now4) #now4没有添加@decorator.
wrapper('1996-09-22') #execute wrapper
					  #now 4:1996-09-22