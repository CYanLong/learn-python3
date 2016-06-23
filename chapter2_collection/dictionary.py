'''
Dictionary是Python的内置数据类型之一.
它定义了键和值之间一对一的关系.

Dictionary没有元素顺序的概念.
Dictionary
'''
d = {"server": "mpilgrim", "database": "master"}
print(d)

print(d["server"])
print(d["database"])
#keys, values, items函数.
#keys方法返回一个包含所有键的list,
#这个list没按dictionary定义的顺序输出.(dictionary中元素是无序的)

#values方法返回一个包含所有值的list.
#items方法返回一个形如(key, value)组成的tuple的list.包含所有的元素.
print(d.keys()) #dict_keys(['返回database', 'server'])
print(d.values()) #dict_values(['master', 'mpilgrim'])
print(d.items()) #dict_items([('database', 'master'), ('server', 'mpilgrim')])

#修改Dictionary.
d["database"] = "pubs"

#添加新值.
d["uid"] = "sa"

#del 允许您使用一个key从一个dictionary中删除独立的元素.
del d["uid"]

#clear方法清除所有的元素.
d.clear()


