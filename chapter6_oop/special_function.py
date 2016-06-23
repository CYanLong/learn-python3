'''专用方法.专用方法是在特殊情况下
	或当使用特别语法时由Python替你调用
	的,而不是在代码中直接调用。
	它提供了一种机制,可以将非方法调用语法映射到
	方法调用上.
	1、__str__专用方法.
	2、__iter__, __next__
	3.__getitem, __setitem__
	4.__call__
	5.__len__

'''
#18013820100
class Student(object):
	def __init__(self, name):
		self.name = name

print(Student("ChenYanlong")) #<__main__.Student object at 0x01D95B70>

#1.通过__str__专有方法,我们可以定制返回的字符串结果.

class Student2(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return "name:" + self.name

print(Student2("ChenYanlong")) #name:ChenYanlong

#2.通过__iter__和__next__专有方法可让一个类可用于for ... in 循环.
#类似于list或tuple,

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10:
			raise StopIteration()
		return self.a

for n in Fib():
	print(n)

#3.通过__getitem__我们可以时一个容器类具有list或tuple的[]操作.

class Fib2(object):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

f = Fib2()
print(f[5])
print(f[0])

#我们还可以继续增强__getitem__,使其具备切片功能.

class Fib3():
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			li = []
			for x in range(stop):
				a, b = b, a + b
				if x >= start:
					li.append(a)
			return li

print("---")
f = Fib3()
print(f[1:5])
print(f[:5])


#5.与__getitem__方法对应的是__setitem__,把对象视list或dict对集合赋值.

class MyDict(object):

	def __init__(self):
		self.dict = {}

	def __setitem__(self, key, value):
		self.dict[key] = value

	def __getitem__(self, key):
		return self.dict[key]

md = MyDict()
md["name"] = "ChenYanlong"
print(md["name"])


#6.__call__专有方法
#一个对象实例可以有自己的属性和方法,当我们调用
#实例方法时,我们用instance.method()来调用.
#我们可以通过__call__方法使得直接调用实例,就像调用一个方法一样.
#instance()

class Person(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print("My name is " + self.name)

p = Person("ChenYanlong ")
p() #My name is ChenYanlong

#7.__len__ 如果你定义的类表现为拥有类似长度的东西,不要定义getLength,定义__len__并使用len(instance)

class MyList(object):

	def __init__(self):
		self.list = []

	def __len__(self):
		return len(self.list)
	def __setitem__(self, index, value):
		self.list.insert(index, value)
	def __getitem__(self, index):
		return self.list[index]

ml = MyList()
ml[0] = "My"
print(len(ml)) #1



