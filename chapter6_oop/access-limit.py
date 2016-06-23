'''访问限制.
	如果想让内部属性不被外部访问,可以在属性的名称
	前面加两个下划线__.这样,这个属性就是私有的了.
	只能在内部可以访问到.
'''

class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print("%s: %s" % (self.__name, self.__score))

s = Student("ChenYanlong", 100)
s.print_score() #ChenYanlong 100

#这样,我们无法在外部访问到了.
#print(s.name)
