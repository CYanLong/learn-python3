'''
4.6:and和or的特殊性质.
在Python中,and 和 or 执行布尔逻辑演算,但它们并不返回布尔值,而是返回
实际进行比较的值之一.

在使用and时,在布尔环境中从左到右演算表达式的值.
0, '', [], {}, None 在布尔环境中为假;其他任何东西都为真。

如果布尔环境中的所有值都为真,那么and返回最后一个值.
如果布尔环境中的某个值为假,则and返回第一个假值.
'''

#如果布尔环境中的所有值都为真,那么and返回最后一个值.
print('a' and 'b') #'b'
print('a' and 'b' and 'c') #c

#如果布尔环境中的某个值为假,则and返回第一个假值.
print('' and 'b') #''

'''
2.or 的使用.
在使用or时,在布尔环境中从左到右演算值.
如果有一个值为真,or立即返回该值.
如果所有的值都是假值,or返回最后一个假值.

'''
print('a' or 'b') # 'a'
print('' or 'b') # 'b'
print('' or [] or {}) # '{}'

'''
3.and-or 技巧.
下面的使用看起来类似与 三目运算符 bool ? a : b;
bool and x 当bool为1(真)时,值为x  
x or y 只要x不为假,则返回x
'''
a = "first"
b = "second"
print(1 and a or b) #first
print(0 and a or b) #second