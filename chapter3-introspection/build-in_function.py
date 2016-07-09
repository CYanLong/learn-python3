'''
4.3. 使用type、str、dir和其它内置函数

Python有小部分相当有用的内置函数.
除这些函数外,其他所有的函数都被分到了各个模块中.

type, str, dir和其他的Python内置函数都归组到了__buildin__
这个特殊的模块中.你可以认为Python在启动时自动执行了from __buildin__ import *.
此语句将所有的"内置"函数导入该命名空间,所以在这个命名空间中可以直接使用
这些内置函数.


'''
'''
1.type函数.type函数返回任意对象的数据类型.

type可以接受任何东西作为参数并返回它的数据类型.
整形,字符串,列表,字典,元组,函数,类,模块,甚至类型对象.
'''
if __name__ == '__main__':
	print(type(1)) #<class 'int'>
	
	li = []
	print(type(li)) #<class 'list'>

'''
2.str函数
str将数据强制转换为字符串.每种数据类型都可以强制转换为字符串.
'''

print(str(1))

horsemen = ['war', 'pestilence', 'famine']
print(horsemen)

horsemen.append('Powerbuilder')
print(str(horsemen))

'''
3.dir函数.
dir函数可以返回任意对象的属性和方法列表
'''
li = [] #list
print(dir(li))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__iadd__', '__init__', '__iter__', 
'__len__', '__lt__', '__new__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 
'reverse', 'sort' ...]
'''


d = {} #dict
print(dir(d))
'''
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values' ...]
'''


'''
4.callable函数.
它接收任何对象作为参数,如果参数对象是可调用的,返回True;否则返回False..
'''
