'''
4.5 过滤列表.

过滤列表语法:
[mapping-expression for element in source-list if filter-expression]
以if开头的是过滤器表达式.任何经过滤器表达式演算值为真的元素都可以包含
在映射中。否则不会进入映射表达式。 更不会包含在输出列表中
'''

li = ["a", "mpilgrim", 'foo', 'b', 'c', 'd', 'd']
li_1 = [elem for elem in li if len(elem) > 1]
print(li_1) #["mpilgrim", 'foo']

li_2 = [elem for elem in li if elem != "b"]
print(li_2) #["a", "mpilgrim", 'foo', 'c', 'd', 'd']

#这里过滤掉不唯一的元素。
li_3 = [elem + '_end' for elem in li if li.count(elem) == 1]
print(li_3)