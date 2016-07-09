''' 
1.Python函数可以返回"多个值"
如下函数定义,我们可以返回多个值,用 ',' 隔开.
并且在调用函数时,可以接受多个值.

但看最后两行代码,当我们用一个值去接受两个函数返回值时
发现value为一个tuple.
没错,python的函数返回值还是只有一个,只不过我们可以
写成看起来有多个返回值的样子.这时,函数会返回一个tuple.
'''

def move(x, y, step = 1):
	nx = x + step
	ny = y + step
	return nx, ny

nx, ny = move(3, 4, step = 5)
print("nx = %s ny = %s" % (nx, ny)) #nx = 8 ny = 9

value = move(3, 4, step = 5)
print(value) #(8, 9)

