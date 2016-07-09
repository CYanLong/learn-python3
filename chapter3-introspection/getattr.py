'''
4.4:getattr()函数

getattr()函数 的doc:

getattr(object, name[,default]) -> value

Get a named attribute from an object;
getattr(x,'y') is equivalent to x.y.
When a default argument is given, it is returned when the attribute doesn't exist.
'''
if __name__ == "__main__":
	
	li = ["Larry", "Curly"] #list
	
	'''该语句获取列表的pop方法的引用.
	 注意该语句并不是调用pop方法.'''
	print(li.pop) #<built-in method pop of list object at 0x007CC198>
	
	'''
	该语句也是返回pop方法的引用.但此时,
	方法名称是作为一个字符串参数传递给getattr函数的。
	getattr可以返回任何对象的任何属性。在这里,对象是一个list,属性是pop方法.
	'''
	print(getattr(li, "pop"))

	'''进一步,getattr的返回值是方法,然后你可以调用它.就像直接使用li.append("Moe")'''
	getattr(li, "append")("Moe")

	'''在这里getattr()函数作用于dict对象'''
	print(getattr({}, "clear"))#<built-in method clear of dict object at 0x00761990>

	'''理论上,getattr可以作用于元组(tuple),但是由于元组没有方法,所以不管指定什么属性都会出错'''
	getattr((), "pop") #AttributeError: 'tuple' object has no attribute 'pop'