'''总结:面型对象
	一:继承和多态:
		Python支持多继承.
		由于Python语言的动态类型,变量没有类型.
		所以Python的多态不需要继承关系(鸭子类型)
	二:成员
		1.类成员(静态成员).
			1).类方法:方法的第一个参数不是self.
			2).类变量:直接在类声明内部定义的字段(没有使用self并且不再任何方法体内)
		2.实例成员
			1).实例成员变量:通过self关键字创建的.(主要在__init__方法中)
			2).实例成员方法:方法的第一个参数是self.
	三:访问权限:在属性前面加两个下划线 '__'可将属性设为私有.
	四:专有方法:__str__, __iter__, __next__, __getitem__, __setitem__,
				__getattr__,__call__, __len__
	五:动态修改类和对象与slots：
		1,我们可以简单并且动态的给已经定义或创建好的类和对象增加任意属性和
			方法
		2、我们可以在类中定义__slots = (tuple)类限制动态的添加.
	六:类型.
		虽然Python是动态类型语言,但它仍然是强类型语言.所以,在Python中,
		每一个变量依旧有自己的类型.并且,在Python中,包括基本字面量,函数对象等都是class类型
		1.并且Python中提供关键字int, str来表示 字面量 基本类型
		 type("str") == str ==> True #<class 'str'>
		2.函数/方法对象:
			1.type(abs) #<class 'builtin_function_or_method'>
			2.type(func) #<class 'function'>
		3.对象的类型:
			type(d) #<class 'dict'>
		4.类的类型
			type(dict) #<class 'type'>

		我们可以通过type得到一个事物的具体类型.

		在继承关系下,我们通过isinstance(instance, class-type)来判断
		一个对象是否是class-type体系下的.

	七:元类.(metaclass)
		1.type()函数除了可以返回对象的类型外,还可以动态的定义一个类
			type('class-name', (super-class,), dict(成员名=值))将返回一个类.
		2.我们可以通过继承type来定义metaclass.这个之后,这个类就是元类的.
			通过元类的__new__(cls, name, bases, attrs)方法,我们可以在定义一个
			目标类的时候为其增加或修改一个成员.(ORM框架)
		
'''