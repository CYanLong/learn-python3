'''
本章总结:
	本章内容为Python的内置容器:dictioary, list, tuple.

	一:dictionary:
		1.定义dictionary: d = {"k1": "v1", "k2": "v2"}
		2.取值: 
			1.根据key取值: value = d["key"]  若不存在key,会报错.
			2.d.keys(), d.values(), d.items() 分别返回dict的所有key,所有values,所有(key,value)的list. 
		3.删除:
			1. del d["key"] 删除单值
			2.d.clear() 清空
 	
 	二:list:
 		1.创建list: li = ["a", "b", "c"]
 		2.取值: list取值只能根据下标,很像数组.
 			1.取单值: li[n] :取出第n个值.
 			2.分割list(splice):li[m:n] 得到m~n之间的list.
 		3.添加:
 			1.添加单个值:li.append(value)
 			2.添加一个list:li.extend(li)
 		4.删除:
 			1.li.remove("value") 删除首次出现的元素.
 			2.li.pop() 删除最后一个元素并返回.
 		5.在list中搜索: value in li 返回boolean值判断一个值是否在list中.
 		6.list运算:
 			1. '+' 运算: list = list + otherlist  等效于: list.extend(otherlist)
 			2. '*' 重复器: li = [value1, value2] * n  等效于: li = [value1, value2]+.n个相加.+[value1, value1]
 		7.映射list:
 			对list中的每一个元素应用一个函数,从而将一个list映射成另一个list.
 			li = [1, 2, 3]
 			newli = [elem*2 for elem in li] #[2, 4, 6]
 		8.list和字符串的转化:
 			1.将list转化为字符串:
 				字符串的join(list)方法接收一个list,返回此list的字符串形式,以此字符串为分隔符.
 				";".["a", "b"] ==> "a;b"
 			2.将字符串转化为list:
 				字符串的split("delimiter", n)方法接收delimiter和可选的分割次数,
 				将字符串按指定delimiter分割成list.
 				"a;b;c".split(";") ==> ["a", "b", "c"]

 	三:tuple
 		tuple是不可变的list,一旦创建了tuple,就不能以任何方式改变它.
 		tuple主要是用来遍历,和list一样,tuple支持下标访问和splicer.
 		创建tuple时与list不同,使用() 
 			tuple = ("a", "b", "c")
 	四:格式化字符串和字符串连接
 		格式化字符串可以往含 '% '字符串中插入任意类型的值.
 		而字符串连接符只能连接多个字符串类型,这一点和Java不同.
'''	