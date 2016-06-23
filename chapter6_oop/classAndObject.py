'''类和实例
	一句话描述类与对象:
		类是抽象的模板,而实例是根据类创建出来的一个个具体的对象.
	
'''
#定义类.
class Student(object):
	pass

#创建对象,就像函数调用一样.
bart = Student()

#类名指向类本身.
print(Student) #<class '__main__.Student'>
print(bart) #<__main__.Student object at 0x017C5BF0>


