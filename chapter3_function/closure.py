'''
闭包:定义内部函数,并将内部函数做为返回值.
注意:当在一个外部函数中定义多个内部函数时,可能会共享外部函数的变量.
此时容易出现问题.
'''

#我们在外部函数lazy_sum中又定义了sum,
#内部函数sum可以引用外部函数lazy_sum的参数和局部变量.
#当lazy_sum返回函数sum时,相关参数和变量都保存在
#返回的函数中.

#当一个函数返回了一个函数后,其内部的局部变量
#还被新函数引用.
def lazy_sum(*args):
	def sum():
		s = 0
		for n in args:
			s = s + n
		return s
	return sum

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1, f2, f3 = count() #返回三个函数.

print("f1 = %s, f2 = %s, f3 = %s " % (f1(), f2(), f3()))
#f1 = 9, f2 = 9, f3 = 9

'''
上面全部返回了9.原因在于返回的函数引用了变量i,但它并非
立即执行.等到3个函数都返回时,它们所引用的变量i已经变成了3.

返回闭包时牢记一点:返回的函数不要引用任何循环变量.
'''

def count2():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1, 4):		
		#fs中存放的是函数g.但此时g的外围函数为f.并且g是f唯一的内部函数.
		#即g中引用的j虽然是f的,但只有g一个函数在用.
		fs.append(f(i)) #在这里,f函数已经被调用.
	return fs

ff1, ff2, ff3 = count2()
print("ff1 = %s, ff2 = %s, ff3 = %s" % (ff1(), ff2(), ff3())) #ff1 = 1, ff2 = 4, ff3 = 9

