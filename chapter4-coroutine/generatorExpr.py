'''
generator expressions(生成器表达式)： 
	生成器表达式提供以一种简洁的语法去创建一个生成器对象。
	生成器表达式与list列表解析式在语法上很相似，但并后者有更好的性能，内存使用率。

'''
g = (n for n in range(3))
print(g) # <generator object <genexpr> at 0x01FB1C00>
next(g)

# equivalent to:
def Range3():
	n = 0
	while n < 3:
		yield n
		n += 1

gr = Range3() # <generator object Range3 at 0x01FB1D20>
print(gr)
next(gr)
