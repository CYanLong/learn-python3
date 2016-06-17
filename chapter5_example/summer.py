'''
总结:example5.1.py中涉及的知识点:

一:关于面向对象方面:
  1、类方法的第一个参数永远都是self.包括__init__
  2、当子类和父类都定义了__init__()方法,子类的__init__()一定要显示调用父类的__init__方法.
  并且当从你的类中调用父类的一个方法时,必须包括self参数.
  3.对类进行实例化只需调用类就好了,就好像它是一个函数一样.传入定义在__init__方法中的参数.
  4.要在类内部引用一个数据属性,使用self作为限定符.数据属性(成员变量)定义在__init__方法中.
  	类属性定义在所有方法外部.(见 field.py)
  5.每个对象都有__class__属性,得到所属的类.
  6.专用类方法.专用方法是在特殊情况下或当使用特别语法时由Python替你调用的.而不是在代码中直接调用.
  	它提供了一种方法,可以将非方法调用语法映射到方法调用上.
  	1).__getitem__专用方法:
  		例:def __getitem__(self, key): return self.data[key]
  			我们可以直接调用此对象的引用 value = f["name"](f为此方法所在的对象)
  			暗地里,Python已经将这个语法转化为f.__getitem__("name").
  	2).类似的,当调用 f["genre"] = 32 时会调用f.__setitem__(self, genre, 32).
  	3).__getitem__和__setitem__将一个对象"打扮"成一个dict.	
  	4).__repr__, __cmp__, __len__ ...
  	总结:专有方法意味着任何类可以像字典一样保存键-值对,只要定义__setitem__方法.
  		任何定义了__cmp__方法的类可以用==进行比较.
  		并且如果你的类表现为拥有类似长度的东西,不要定义getLength方法,而定义__len__方法,并使用len(isntance).
  	5).私有函数
  		私有函数不可以从它们的模块外面被调用.
  		私有类方法不能够从它们的类外面被调用.
  		私有属性不能够从它们的类外面被调用.

  		如果一个Python函数,类方法,或属性的名字以两个下划线开始(但不是结束), 它是私有的.
'''	

'''
	二:关于文件处理.
		1.open,打开在磁盘上的文件,open("filename")返回一个文件对象.
		f = open("filename", "mode")
		f.tell(), f.seek(length, mode), f.read(length)
		f.close()
		正确的处理文件:
		try:
			fsock = open("filename", "mode", "cache") #如果在这里发生异常,直接执行except.
			#一旦文件通过open函数被成功地打开,我们应该绝对保证把它关闭.
			try:
				fsock = seek(-128, 2) #如果在这里发生异常,会执行finally和except.
				tagdata = fsock.read(128)
			finally:
				fsock.close()
		except IOError:
			pass
    2.写入文件 write_file.py
    3.目录/路径操作.
  三:关于modules.
    首先,模块也是对象. 见 modules.py
		 
'''