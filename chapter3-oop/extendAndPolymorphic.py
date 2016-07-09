'''继承和多态.
	在OOP程序设计中,当我们定义了一个class的时候,
	可以从某个现有的class继承,新的class称为子类(subclass)
	而被继承的class称为基类,父类或超类(Base class, Super class)
   Python支持多继承.

'''

class Animal(object):
	def run(self):
		print("Animal is running...")

class Dog(Animal):
	pass

class Cat(Animal):
	pass

d = Dog()
c = Cat()

d.run() #Animal is running...
c.run() #Animal is running...

'''子类可以重定义从父类继承来的方法.
'''
class Dog2(Animal):
	def run(self):
		print('Dog is running')

class Cat2(Animal):
	def run(self):
		print('Cat is running')

d2 = Dog2()
c2 = Cat2()

d2.run() #Dog is running
c2.run() #Cat is running

'''多态
	Python这样的动态类型语言,变量本身是没有类型的
	(没有类型的概念),只有变量值才有类型.


	在Java中,类型的检查涉及两方面.
		1.编译期的变量本身的类型(静态类型)检查
		2.运行期的变量值的类型(动态类型)检查
	所以,Java要求多态的实现必须具有继承关系(静态检查).

	而由于Python本身没有静态类型(变量的类型)这个概念.
	所以Python多态的实现不需要具有继承关系.只要动态类型符合即可.
'''

#这个方法不仅可以接受animal的子类,只有一个对象
#有run方法,就可以运行.
def run_twice(animal):
	animal.run()
	animal.run()

run_twice(d2) #Dog is running
			  #Cat is running
run_twice(c2) #Dog is running
			  #Cat is running

class other_class(object):
	def run(self):
		print("other_class run.. ")

o = other_class()
run_twice(o) #o对象与animal并没有继承关系.

'''继承关系下的类型判定.
	在继承关系中,如果一个实例的数据类型是某个子类,那
	它的数据类型也可以被看做是父类.
'''
class Person(object):
	pass

class Man(Person):
	pass

p = Person()
m = Man()

#m对象的类型即使Man,又可以是其超类Person.
print(isinstance(m, Person)) #True



'''Python的多继承.(MixIn)
	在设计类的继承关系时,通常,主线都是单一继承下来的.
	例如,Dog继承Mammal,Mammal继承Animal.
	如果需要"混入"额外的功能,通过多重继承就可以实现.
	比如,让Dog除了继承自Mammal外,同时继承Runnable.
	这种设计通常称之为MixIn.

	MixIn的目的就是给一个类增加多个功能,这样,在设计
	类的时候,我们优先考虑通过多重继承来组合多个MixIn
	的功能.而不是设计层次复杂的继承关系.

	在Java这样的单继承语言中,要使一个类同时"混入"多个
	功能,需要利用Java的多实现(implements)来完成.


'''

class Animal(object):
	pass

#哺乳类
class Mammal(Animal):
	pass

#鸟类
class Bird(Animal):
	pass


class Runnable(object):
	def run(self):
		print("running..")

class Flyable(object):
	def fly(self):
		print("fly...")

#狗类:属于哺乳类和可跑类型.
class Dog(Mammal, Runnable):
	pass

#鹦鹉类:属于鸟类和可飞类型.	
class Parrot(Bird, Flyable):
	pass
