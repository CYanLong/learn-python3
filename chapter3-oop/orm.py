'''ORM原型.
	首先,要编写底层模块的第一步,是先把调用接口写出来.
	如下,我们希望使用者进行如下ORM操作.其中Model, IntegerField,
	StringField.等都是ORM框架提供的.

	1、Field体系:Field(StringField, IntegerField)等用来描述数据库中的字段.
		每个Field都有一个字段名(name)和字段类型(column_type).
	2、定义Model,每个entity都需要继承Model.
	3、Model使用了Metaclass.我们需要定义一个Metaclass,作用于每个继承自
		Model的entity类.在Metaclass中,我们通过attrs遍历中entity中定义
		的所有Field.得到{变量名=Field对象(字段名和字段类型)}的dict.
		并将此dict以__mapping__名的类变量添加到目标entity中.
	4、
'''
#首先定义Field.
class Field(object):

	def __init__(self, name, column_type):

		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)

#在Field的基础上,进一步定义各种类型的Field.
class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

#编写ModelMetaclass
class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		print("ModelMetaclass.__new__()")
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print("Found model: %s" % name)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print("Found mapping: %s ===> %s" % (k, v))
				mappings[k] = v
		#将原来的删掉.
		for k in mappings.keys():
			print("pop: %s" % k)
			attrs.pop(k)
		attrs['__mappings__'] = mappings
		attrs['__table__'] = name
		return type.__new__(cls, name, bases, attrs)

print("===")

class Model(dict, metaclass=ModelMetaclass):
	
	def __init__(self, **kw):
		print("Model.__init__ invoke")
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		print("getattr invoke %s" % key)
		try:
			return self[key]
		except KeyError:
			raise AttributeError("Model object has no attribute %s" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name) 
			params.append("?")
			args.append(getattr(self, k, None))
		print('fields: %s' % fields)
		print('params: %s' % params)
		print('args: %s' % args)
		sql = 'insert into %s (%s) values (%s) ' % (self.__table__, ','.join(fields), ','.join(params))
		print(sql)


print("---")
class User(Model):
	id = IntegerField('t_id')
	name = StringField('t_username')
	email = StringField('t_email')
	password = StringField('t_password')

u = User(id=1234, name='Chen', email='test@orm.org', password='my-pwd')

u.save()