'''
lambda表达式/匿名函数.
	1.匿名函数有个限制,只能有一个表达式,不用写return.
	  返回值就是该表达式的结果.
	2.匿名函数就是一个函数对象,可以将lambda
	  表达式传给变量.
'''

#map的第一个参数接收一个函数.通过lambda实现定义和使用同时进行.

print(list(map(lambda x: x * x, [1, 2, 3, 4]))) #[1, 4, 9, 16]

#

def build(x, y):
	return lambda: x * x + y * y

print(build(3, 4)) #<function build.<locals>.<lambda> at 0x01807228>
f = build(3, 4)
print(f()) #25