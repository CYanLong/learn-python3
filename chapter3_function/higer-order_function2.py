'''高阶函数(map, reduce, filter)
	
	1.map函数
		接受两个参数,一个是函数,一个是Iterable.
		map函数将依次将传入的参数作用到Iterable的每个元素上,以函数的返回值作为新容器的元素.

	2.reduce函数.
		reduce接收一个函数和一个容器,这个函数必须接收两个参数,
		reduce将结果继续和序列的下一个元素做累积运算.
	3.filter函数.
		filter同样接收一个函数和一个容器,这个函数的必须返回布尔值.
		最终filter会过滤掉函数返回值为假的元素.

	4.sorted函数
		sorted默认可以进行数字和字符串比较,可以接受函数
		和reverse=boolean 来控制排序算法和排序次序.
'''

def f(x):
	return x * x
#map的返回结果是一个Iterator.
r = map(f, [1, 2, 3])
print(r) #<map object at 0x009CB4D0>
#可以通过list()函数让它把整个序列都计算出来.
print(list(r)) #[1, 4, 9]

#试想,如果没有map,我们需要些很长的代码来实现.
li = []
for n in [1, 2, 3]:
	li.append(f(n))
print(li)

#另一个例子.
list(map(str, [1, 2, 3, 4])) #['1', '2', '3', '4']


'''reduce
	reduce把一个函数作用于一个序列[x1, x2, x3, ...]上,
	reduce把结果继续和序列的下一个元素做累积计算.
	reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
	要注意,f函数必须且只能有两个参数.
'''
from functools import reduce
def add(x, y):
	return x + y

reduce(add, [1, 2, 3])
#上面的reduce调用过称为:add(add(1, 2), 3) ==> add(3, 3) = 6

#另一个例子
def fn(x, y):
	return x*10 + y

reduce(fn, [1, 2, 3]) #123
#上面的调用过程 ((1*10 + 2)*10 + 3)

#想像以下吧,如果没有reduce,我们该如何实现呢?
def fn2(*numbers):
	index = 0
	while index < len(numbers):
		if index == 0:
			temp = numbers[index]
			index += 1
		temp = temp * 10 + numbers[index]
		index += 1

fn2(1, 2, 3) 


#例子三:把str转化为int.综合了map和reduce.
def char2int(char):
	i = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
	 '6': 6, '7': 7, '8': 8, '9': 9}[char]
	return i

def str2int(str,f = char2int):
	li = map(f, str)
	return reduce(fn, li)

print(str2int("123456"))



'''3.filter()函数.
	filter()跟map()类似,接收一个函数和一个可迭代容器.
	filter()内部会将容器中每个值作用于传入的函数,此函数必须
	返回布尔类型,最终filter返回布尔为真的元素组成的容器.
	
'''

def is_odd(n):
	return n % 2 == 1
#筛选出list中为奇数的值.
print(list(filter(is_odd, [1, 2, 3, 4]))) #[1, 3]


def not_empty(s):
	return s and s.strip()
	#注意,下面的写法不全面, '' 不等于 '  '
	#s != ''

print(list(filter(not_empty, ["1", "  ", ""])))



'''4.sorted
	排序,当我们要比较的对象是数字或字符串时,可以直接比较.
	但当我们要比较对象时,比较算法就需要通过函数来抽象出来.
	我们可以通过sorted函数来比较数字(从小到大),字符串(字典顺序)
	
	当然,sorted函数也是一个高阶函数,我们可以通过传入比较参数来自己定制比较规则.
	sorted还可以传入可选参数reverse=True来控制正序排序还是倒序排序.
'''

print(sorted([36, 5, -12, 9, -21])) #[-21, -12, 5, 9, 36]
print(sorted(["d", "a", "c", "abc"])) #['a', 'abc', 'c', 'd']

#按照绝对值从小到大.
#key指定的函数将作用于list的每一个元素上,并根据
#key函数返回的结果进行排序.
print(sorted([36, 5, -12, 9, -21], key=abs)) #[5, 9, -12, -21, 36]
 
 #传入str.lower函数进行忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

#sorted还有一个参数用来指定正序还是反序排序.
print(sorted([11, 2, 3, 4], reverse=True)) #[11, 4, 3, 2]








