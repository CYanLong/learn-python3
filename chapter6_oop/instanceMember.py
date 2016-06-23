'''实例变量.
	
	1.实例方法只能由对象来调用.所以,在类中编写的
	实例方法第一个参数必须为self.(同样的,在Java中,所以的实例方法的
	一个参数都为this,不同的是,Java会自动帮你写,而Python必须由自己显示声明出来)

		__init__方法.
			__init__方法是实例方法.但它比一般实例方法要特殊一些.
			__init__方法是在对象一创建完后自动调用的.
			有了__init__方法,在创建实例时,就不能传入空的参数.必须参数与__init__匹配的参数.

	2.实例变量
		实例变量是专属于对象的,由于Python的动态性,同一个类的多个对象
		可以有不同的实例变量.
		通过object.field = value 来定义成员变量.
		所以在类内部,只有在实例方法中通过self关键字才能定义成员变量(__init__).

'''

class Student(object):
	def __init__(self, name, score):
		#通过self引用定义的变量为成员变量.
		#由于每一个对象都会调用此方法.
		#所以,我们可以确定每一个此类的对象都有name和score属性.
		self.name = name
		self.score = score

#当对象创建完成后,会执行__init__方法.
s = Student('ChenYanlong', 100)

s.age = 20
print(s.age) #定义成员变量.


'''普通的成员方法调用.
	调用成员方法时,必须使用对象变量名去调用.
	这样,才可以将对象传入成员方法的self参数中.

'''
class Player(object):
	def play(self, something):
		print("%s object play %s" % (self, something))

p1 = Player()
p2 = Player()

p1.play("CF") #<__main__.Player object at 0x017BBDD0> object play CF
p2.play("QQ") #<__main__.Player object at 0x017BBDF0> object play QQ


