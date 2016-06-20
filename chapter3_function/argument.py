'''
Python支持可变参数,关键字参数,关键字命名参数,
		命名参数,默认参数.
'''

'''
1.可变参数:
	实现给定一组数字a, b, c...计算a^2 + b^2 + c^2...
	实现一:函数的参数接收list或tuple,调用时将a, b, c..转化为list或tuple
	实现二:定义可变参数(*argument).调用时直接传值就可以.
可变参数允许你传入0个或任意个参数,这些可变参数在调用时自动组装为一个tuple.
'''
#实现一:
def calc(numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum
#在调用的时候,需要先组装出一个list或tuple
print(calc([1, 2, 3]))
print(calc((1, 2, 3)))

#实现二
def calc2(*numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum
#调用时,直接传值就可以.
calc2(1, 2, 3) #会自动组装成一个tuple.
calc2()

'''
2.关键字参数.
	关键字参数允许你传入任意个含参数名的参数,
	这些关键字参数在函数内部自动组装为一个dict.
	1).命名关键字参数.
'''

def person(name, age, **kw):
	print('name:', name, 'age:', age, "other:", kw)

person('ChenYanlong', 20) #name: ChenYanlong age: 20 other: {}
person('ChenYanlong', 20, city='Harbin', job='Engineer')
#name: ChenYanlong age: 20 other: {'job': 'Engineer', 'city': 'Harbin'}

'''
2.1命名关键字参数:
	对于关键字参数,函数的调用者可以传入任意不受限制的关键字参数.
	为此,我们可以限制关键字参数的名字.
	定义好命名关键字参数后,调用时不可省略命名关键字参数,并且必须使用
	命名参数调用.
'''
#
def person2(name, age, *, city, job):
	print(name, age, city,job)

person2('ChenYanlong', 20, dity='Harbin', job='Engineer')
#下面均会报错.
#person2('ChenYanlong', 20, 'Harbin')
#person2('ChenYanlong', 20)
#person2('ChenYanlong', 20, degree='Bachelor')

'''
3.命名参数
	在调用函数时,可以显示指定参数名.这时,参数顺序可以和声明时不一样.
'''
def person3(name, age, city, job):
	pass

person3('ChenYanlong', 20, job='Engineer', city='Harbin')

'''
4.默认参数:
	在定义函数时,可以指定一个默认的参数值,这样,我们在调用时
	可以不用对此传参.
'''
#计算x的n次方.默认情况下,n=2 即求平方

def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(2)) #4
print(power(2, 3)) #8