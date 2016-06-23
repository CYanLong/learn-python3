'''Python中变量值的类型判断.
	当我们拿到一个变量时,如何判断其指向的数据类型?
		1.type()函数.
			我们观察到,无论是基本数据类型的字面量,
			内置函数,自定义函数,类本身,对象
			type函数都返回class类型.
		2.instance()函数.
'''
#基本数据类型的字面量类型
#可以看到,Python中有int, str等类型.
print(type(123)) #<class 'int'>

print(type('abc')) #<class 'str'>

def func(): 
	pass

#函数类型:function类型.
print(type(func)) #<class 'function'>
print(type(abs)) #<class 'builtin_function_or_method'>


class Person(object):
	pass

p = Person()
#对象类型:对象所属的类.
print(type(p)) #<class '__main__.Person'>
#类的类型:type
print(type(Person)) #<class type>
print(type(int)) #<class 'type'>


'''
'''
print("分割线..")
#无论是123还是456,其类型都是int.
#并且,在Python中,int作为关键字用来表示此类型.
print(type(123) == type(456)) #True 
print(type(123) == int) #True


p1 = Person()
p2 = Person()
#p1和p2都是Person类型
#并且,每个类名都像一个关键字一样用来表示此类的类型.
print(type(p1) == type(p2)) #True
print(type(p1) == Person)  #True

#无论是Python内置的dict类型还是自定义的Person类型
#本质上讲都是一种数据类型(type).
print(type(dict) == type(Person)) #True


print("----")
'''types模块
	基本类型可以直接使用关键字int, str来表示.
	但如果要判断一个对象是否是函数,lambda表达式..时,
	我们需要types模块.
	types模块有很多常量用来表示这些数据类型.
'''
import types;

def fn():
	pass

print(type(fn) == types.FunctionType) #True

print(type(abs) == types.BuiltinFunctionType) #True

print(type(lambda x:x) == types.LambdaType) #True

print(type((x for x in range(10))) == types.GeneratorType) #True



'''isinstance()函数.
	对于class的继承关系来说,使用type()不是很方便.
	我们要判断class的类型,可以使用isinstance函数.
	使用type无法判断一个继承关系下的类型.
'''

class Animal(object):
	pass

class Dog(Animal):
	pass

d = Dog()

print(isinstance(d, Dog)) #True 
print(isinstance(d, Animal)) #True

print("---")

print(type(d)) #<class '__main__'.Dog>
print(Dog) #<class '__main__'.Dog>
print(Animal) #<class '__main__'.Animal>
print(type(d) == Dog) #True
print(type(d) == Animal) #False