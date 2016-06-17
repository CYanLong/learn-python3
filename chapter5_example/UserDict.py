'''
Python 支持数据属性,它是由某个特定的类实例所拥有的数据.
在本例中,每个UserDict实例将拥有一个data数据属性.

'''
class UserDict:
	def __init__(self, dict=None):
		self.data = {}
		if dict is not None: self.update(dict)
		
	def __getitem__(self, key):
		return self.data[key]
	
	def __setitem__(self, key, item):
		self.data[key] = item
	#__repr__是一个专有方法,在当调用repr(instance)时被调用.
	#而repr函数是一个内置函数,它返回一个对象的字符串表示.
	def __repr__(self):
		return repr(self.data)

	#在比较类实例时(==)被调用
	def __cmp__(self, dict):
		if isinstance(dict, UserDict):
			return cmp(self.data, dict.data)
		else:
			return cmp(self.data, dict)

	#在调用len(instance)时被调用.
	def __len__(self):
		return len(self.data)

	

	def clear(self):
		self.data.clear()

	def copy(self):
		if self.__class__ is UserDict:
			return UserDict(self.data)
		#真正字典的copy方法会返回一个新的字典.它是原始字典的原样复制.
		#但UserDict不能简单地重定向到self.data.copy.
		#如果是UserDict调用此方法,也应该返回一个UserDict对象.
		import copy
		return copy.copy(self)

	def keys(self):
		return self.data.keys()

	def items(self):
		return self.data.items()

	def values(self):
		return self.data.values()

