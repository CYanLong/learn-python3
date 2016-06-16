'''
Print methods and doc strings
Takes modules, class, list, dictionary, or string.
'''
def info(object, spacing=10, collapse=1):	
	#获得object对象所有可调用(callable)属性.
	methodList = [method for method in dir(object) if callable(getattr(object, method))]
	#根据collapse的值决定是否换行.最终processFunc得到的值一个函数.
	processFunc = collapse and (lambda s : "".join(s.split())) or (lambda s : s)
	print("\n".join(["%s %s" % (method.ljust(spacing), processFunc(str(getattr(object, method).__doc__))) for method in methodList]))

if __name__ == '__main__':
	li = ['a', 'b', 'c']
	print(info(li))
