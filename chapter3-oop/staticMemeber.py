 '''类成员
	1.静态方法
		静态方法的特定是不需要任何对象的信息.
		类一经定义,这个方法的执行结果就确定下来了.

		所以,我们在定义类方法时,无需将self作为参数.
		在调用类方法时,直接通过classname.methodname()来调用.

	2.静态字段.
		静态字段与静态方法类似,当类一经定义,静态字段
		就已经可以访问,无需使用对象.
		直接在类声明的内部定义的字段就是静态字段,或者说，
		没有使用self关键字并且不再任何方法体内.

'''		


class Connector(object):
	a = 5
	def getConn():
		print("getConn...")

Connector.getConn() #getConn...
print(Connector.a) #5
Connector.a = 'aa' #
print(Connector.a)