'''
	@property把一个getter方法变成属性
	此时@property本身有创建了另一个装饰器@score.setter.
	负责把一个setter方法变成属性赋值.
'''

class Student(object):
	@property
	def score(self):
		print("get property..")
		return self._score

	@score.setter
	def score(self, value):
		print("setter..")
		self._score = value

s = Student()
s.score = 20 #setter... 实际转化为 s.score(20)
print(s.score) #get property.. 实际转化为s.score()
			   #20

