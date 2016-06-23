'''
tuple是不可变的list,一旦创键了tuple,就不能以任何方式改变它.

'''
t = ("a", "b", "mpligrim", "z", "example")

#tuple的元素与list一样按定义的次序进行排序.
print(t[0]) # 'a'
print(t[-1]) # 'example'
print(t[1:3]) #('a', 'mpligrim')

#无法进行下面这些操作.
#t.append("new")
#t.remove("z")
#t.index("example")

'''
tuple的优点:
	1.tuple比list操作速度快.如果定义一个值的常量集,并且唯一要
	做的是不断地遍历它,tuple优于list.
	2.tuple可以在dictionary中被用作key,但list不行.
''' 
