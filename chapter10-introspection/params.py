'''
4.2:Python使用可选参数和命名参数.

可选参数:Python允许函数参数有缺省值.如果调用函数时不使用参数,参数将获得它的缺省值.

命名参数:通过使用命名参数可以任意顺序指定参数.
'''

'''
	这是一个计算n次幂的函数,当调用power(x)时默认计算x的2次幂
	当然,也可以通过power(x, n)调用来决定计算x的n次幂.
'''
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

'''
如下是一个学生注册信息的函数,当一个方法参数很多时,
调用会非常不方便,必须时刻注意参数的顺序.Python提供的
命名参数可以无需关注参数顺序.
'''
def enroll(name, gender, age, city):
	print('name', name)
	print('gender', gender)
	print('age', age)
	print('city', city)

#使用命名参数调用
enroll(name='Chen Yanlong', gender="男", city="Harbin", age = 20)
