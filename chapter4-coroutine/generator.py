'''
生成器：当一个生成器函数被调用时，它不会执行函数体的内容，而是返回一个生成器对象。
		这个生成器对象具有与迭代器对象相同的语意，即可以作用于next(),iter(), for-in 语句。   
		当调用next()时这个函数才开始执行直到遇到yield语句。 被yielded的值作为next()的返回值。
		当没有值可以yield时将抛出StopIteration，表明所有的值都已经被生成。

'''
def foo():
	print("begin")
	for i in range(2):
		print("before yield %s" % i)
		yield i
		print("after yield %s " % i)
	print("end")

f = foo() 
print(next(f)) # begin
   			   # before yield 0
   			   # 0

print(next(f)) # after yield 0
 			   # before yield 1
 			   # 1
print(next(f)) # after yield 1
               # end
               # StopIteration Exception... 

print("----分隔线----")

def fibonacci():
	a = b = 1
	yield a
	yield b
	while True:
		a, b = b, a + b
		yield b

f = fibonacci() #<generator object fibonacci at 0x01170630>
print(f)

it = iter(f)
print(it == f) #True

print(next(f)) #1
print(next(it)) #1


	