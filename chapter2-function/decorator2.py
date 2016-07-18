'''
下面的一个没有使用语法糖的装饰器。
装饰器函数接收被增强的函数，在内部定义一个实现增强
逻辑的函数，并将此函数返回用我们使用。

实现增强逻辑的函数的参数列表应该与被增强函数相同。
这样我们才能和使用原函数一样使用被增强的函数。
'''
def get_text(name):
	return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
	def func_wrapper(name):
		return "<p>{0}</p>".format(func(name))
	return func_wrapper

my_get_text = p_decorate(get_text)
print(my_get_text("John")) #<p>lorem ipsum, John dolor sit amet</p>

'''Python提供的装饰器语法糖。
'''
#我们无需在显示编写 get_text = p_decorator(get_text)
@p_decorate
def get_text2(name):
	return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text2("John"))

def strong_decorator(func):
	def func_wrapper(name):
		return "<strong>{0}</strong>".format(func(name))
	return func_wrapper

def div_decorator(func):
	def func_wrapper(name):
		return '<div>{0}</div>'.format(func(name))
	return func_wrapper

@p_decorate
@div_decorator
@strong_decorator
def get_text3(name):
	return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text3("Cyanlong")) #<p><div><strong> ...