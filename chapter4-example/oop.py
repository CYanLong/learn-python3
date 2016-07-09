'''
5.2:类的定义
Python是完全面向对象的:你可以定义自己的类,从自己的或内置的类继承.

在Python中,类的基类只是简单地列在类名后面的小括号里.
Python支持多重继承.
'''

'''
1.__init__() 初始化
__init__在类的实例创建后被立即调用.它可能会引诱你称之为类
的构造函数.

每个类方法的第一个参数,包括__init__,都是指向类的当前实例的引用.
这个参数总是self.在__init__方法中,self指向新创建的对象.
在其他的类方法中,它指向方法被调用的类实例.
尽管当定义方法时你需要明确指定self,但在调用方法时,你不用指定它.

__init__方法从不返回一个值.
'''
class FileInfo:
	'''Store file metadata'''
	def __init__(self, filename=None):
		print("filename:" + filename)

''' 
2.类的实例化:在Python中对类进行实例化很直接.
只要调用类(就好像它是一个函数),传入定义在__init__方法中的参数.
返回值将是新创建的对象.
'''
if __name__ == '__main__':
	f = FileInfo("/sd")
	print(f.__class__) #<class '__main__.FileInfo'>
	