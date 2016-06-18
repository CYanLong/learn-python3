'''
格式化字符串:
	将一个变量值插入到一个有字符串格式符%s的字符串中.

'''
k = "uid"
v = "sa"
print("%s = %s" % (k, v)) #(k, v)是一个tuple.

'''
字符串格式化与字符串连接的比较
'''

uid = "sa"
pwd = "secret"
print(pwd + "is not a good password for " + uid)
print("%s is not a good password for %s" % (pwd, uid))

userCount = 6
#字符串格式化通常将%s替换成%d即可处理整数.
print("Users connected : %d" % (userCount,)) #当定义一个只包含一个元素的tuple时逗号是必须的.

#试图将一个字符串同一个非字符串连接会引发一个异常. TypeError:cannot concatenate 'str' and 'int' objects.
#与字符串格式化不同,字符串连接只能在被连接的每一个都是字符串时起作用.
print("Users connected" + userCount)
