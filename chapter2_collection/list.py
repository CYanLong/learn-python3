'''
List是Python中使用最频繁的数据类型.

'''
#list是一个用方括号包括起来的有序元素的集合.
li = ["a", "b", "mpilgrim", "z", "example"]

#使用起来和数组很像.
print(li[0]) #a

#负数索引从list的尾部开始向前计数来存取元素.
#对于负数索引,可以这样理解:li[-n] = li[len(li) - n]
#li[-1] = li[5-1] = li[4]
print(li[-1]) #example

#splice. 
print(li[1:3]) #["b", "mpligrim"]
print(li[1:-1]) #["b", "mpligrim", "z"]
print(li[:3]) #["a", "b", "mpligrim"]
print(li[3:]) #["z", "example"]
#与原始的名为li的list不同,它是一个新的list.
#所以,li[:]可以用来生成一个list完全拷贝
print(li[:]) #["a", "b", "mpilgrim", "z", "example"]

#向list中添加元素.
#1.append向list未尾追加单个元素.
li.append("new")

#2.insert将单个元素插入到list中.
li.insert(2,"new")

#3.extends用来连接list.
li.extend(["tow", "elements"])


#append和insert的差别
li = ["a", "b", "c"]
li.extend(["d", "e", "f"])
print("len = %s, elements = %s " % (len(li), li)) #len = 6, elements = ["a", "b", "c", "d", "e", "f"]

li = ["a", "b", "c"]
li.append(["d", "e", "f"])
print("len = %s, elements = %s" % (len(li), li)) #len = 4, elements = ["a", "b", "c", ["d", "e", "f"]]


#在list中搜索.
#print(li.index("example")) #ValueError list.index(x): x not in list
#要测试一个值是否在list内,使用in.
print("c" in li) #True

#从list中删除元素.
#1.remove方法从list中删除首次出现的元素.如果未找到,抛出异常.
li.remove("a")
#2.pop删除list的最后一个元素,然后返回删除元素的值.
print(li.pop())

#list运算符.
li = ["a", "b", "mpligrim"]
#List也可以用+运算符连接起来. list = list + otherlist ==> list.extend(otherlist)
#但+运算符把一个新(连接后)的list作为值返回,而list.extend()在原list基础上添加.
li = li + ["example", "new"]
li += ["two"]
# * 运算符可以作为一个重复器作用于list.
#li = [1, 2] * 3 等同于 li = [1,2] + [1,2] + [1, 2]
li = [1,2] * 3


'''
映射list.
list解析,可以通过对list中的每一个元素应用一个函数,从而将一个list映射为另一个list.
对list的解析并不改变原始的list.
'''
li = [1, 9, 8, 4]
print([elem*2 for elem in li]) #[2, 18, 16, 8]
print(li) #[1, 9,8, 4]

'''
连接list与分割字符串.

1.join:
	下面的join方法将list中的元素连接成单个字符串,
	每个元素用一个分号隔开.最前面的分割符可以是任意字符串.

	join只能用于元素是字符串的list.
2.split:
	split("delimiter", n):delimiter为分隔符,n为想要分割的次数.
	最终返回一个list.
'''	
params = {"uid": "sa", "pwd": "root", "charset": "utf-8"}

print(";".join(["%s=%s" % (k, v) for k, v in params.items()]))
#uid=sa;pwd=root;charset=utf-8

li = ["server=mpligrim", "uid=sa", "database=master", "pwd=secret"]
s = ";".join(li)
print(s) #server=mpligrim;uid=sa;database=master;pwd=secret
print(s.split(";")) #["server=mpligrim", "uid=sa", "database=master", "pwd=secret"]
print(s.split(";", 1))#["server=mpligrim", "uid=sa;database=master;pwd=secret"]