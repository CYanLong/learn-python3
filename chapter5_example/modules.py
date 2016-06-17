import sys
'''sys.modules是一个字典(dict)
	它包含了从程序运行起导入的所有模块.
	key为模块名,value为模块对象.
'''
print("\n".join(sys.modules.keys()))

'''
每个Python类都拥有一个内置的类属性__module__,它定义了这个类的模块的名字.
它与上面的sys.modules字典复合使用,可以得到定义了某个类的模块的引用.
'''
from example5 import MP3FileInfo
print(MP3FileInfo.__module__)