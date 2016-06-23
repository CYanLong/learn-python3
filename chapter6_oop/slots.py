'''使用__slots__.
	通常情况下,当我们定义了一个class,
	创建了一个class的实例后,我们可以给该
	实例绑定任何属性和方法.
'''

class Student(object):
	pass

s = Student()
#动态的给一个对象添加属性.
s.name = 'ChenYanlong'
print(s.name) #ChenYanlong

def set_age(self, age):
	self.age = age

from types import MethodType

#动态的给一个对象添加方法.
s.set_age = MethodType(set_age, s) #给实例绑定一个方法.
s.set_age(20)
print(s.age) #20

#我们也可以动态的给类添加属性和方法.

def set_score(self, score):
	self.score = score

#动态的修改一个类,为其增加一个成员方法.
Student.set_score = set_score
Student.gender = '男'
#这样,所有的对象都可以访问到.
s.set_score(100)
print(s.score) #100
print(s.gender) #男

'''但是,我们可以通过__slots__来限制对象动态修改其数据结构.
	__slots__对子类没有限制.
'''

class Teacher(object):
	__slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称.

t = Teacher()
t.name = 'ChenYanlong'
t.age = 20

#会失败.
#t.gender = '男'
