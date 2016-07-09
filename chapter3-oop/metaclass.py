'''
'''
class Hello(object):
	def hello(self, name="world"):
		print("Hello, %s" % name)

h = Hello()
h.hello()
#type()函数可以查看一个类型或变量的类型.
#Hello是一个class,它的类型就是type.
print(type(Hello)) #<class 'type'>
#而h是一个实例,它的类型就是Hello
print(type(h)) #<class '__main__.Hello'>

'''class是运行时动态创建的,而创建class的方法就是使用type.函数.
	type()函数既可以返回一个对象的类型,又可以创建出新的类型.
	要动态创建一个class对象,type()函数必须一次传入3个参数:
	  1.class的名称
	  2.继承的父类集合.tuple结构
	  3.class的方法名称和函数绑定. dict结构.
'''

def fn(self, name="world"):
	print("Hello %s" % name)
Hello2 = type('Hello2', (object,), dict(hello=fn)) #创建Hello class.

h2 = Hello2()
print(type(Hello2)) #<class 'type'>
print(type(h2)) #<class '__main__.Hello2'>

'''metaclass/元类.
	先定义类,在创建对象.对应的,先定义metaclass,再创建类.
	metaclass允许你创建类或动态修改类.
'''

class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		#attrs为类的方法集合.(这个方法是由来调用的)
		#这条语句将增加一个方法,方法名为add,方法实现为=后面的语句.
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

#当我们传入关键字参数metaclass时,它指示Python解释器在创建MyList
#时,要通过ListMetaclass.__new__()来创建.
#在这里,ListMetaclass将为MyList添加一个add方法.
class MyList(list, metaclass=ListMetaclass):
	pass

myList = MyList()
myList.add("1")
print(myList)