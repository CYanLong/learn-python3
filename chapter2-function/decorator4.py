'''Passing arguments to decorators
	给装饰器传递参数.
'''

def tags(tag_name): # decorator generator.
	def tags_decorator(func):
		def func_wrapper(name):
			return "<{0}>{1}<{0}>".format(tag_name, func(name))
		return func_wrapper
	return tags_decorator

@tags("p")
def get_text(name):
	'''returns some text'''
	return "Hello" + name

'''包装函数没有携带原函数的名字，模块和docstring.
	这些数据全被包装函数覆盖掉了。
	使用functools的wraps装饰器可以消除这个影响。
'''

print(get_text.__name__) # func_wrapper

from functools import wraps

def tags2(tag_name):
	def tags_decorator(func):
		@wraps(func)
		def func_wrapper(name):
			return "<{0}>{1}<{0}>".format(tag_name, func(name))
		return func_wrapper
	return tags_decorator



