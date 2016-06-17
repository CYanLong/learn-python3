class Counter:
	count = 0 #类属性定义在外面.
	def __init__(self): #实例属性定义在__init__方法中
		self.__class__.count += 1

if __name__ == '__main__':
	print(Counter.count) #0
	c1 = Counter()  
	print(Counter.count) #1
	c2 = Counter()
	print(Counter.count) #2