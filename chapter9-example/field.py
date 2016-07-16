class Counter:
	count = 0 #类属性定义在所有方法外面.
	def __init__(self):  #实例属性定义在__init__方法中.
		self.__class__.count += 1

if __name__ == '__main__':
	print(Counter.count) #类属性先于任何对象创建.
	c1 = Counter()
	print(Counter.count)
	c2 = Counter()
	print(Counter.count)