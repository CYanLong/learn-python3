'''
我们不仅可以增强(装饰)函数，还可以增强定义在对象中的方法。

其实，方法就是一类第一个参数为指向当前对象的引用的函数。
'''
def p_decorator(func):
	def func_wrapper(self):
		return '<p>{0}</p>'.format(func(self))
	return func_wrapper

class Person(object):
	def __init__(self):
		self.name = "ChenYanlong"
		self.family = "Doe"

	@p_decorator
	def get_fullname(self):
		return self.name + "" + self.family

my_person = Person()
print(my_person.get_fullname())

''' *args and **kwargs
	一个更好的方法是将 *args 和 **kwargs作为wrapper
	函数的参数。它能接收任意数量的参数和关键字参数。
'''