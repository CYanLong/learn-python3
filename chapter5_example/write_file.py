'''
有两种基本的文件模式:
	1.追写(Append)模式将数据追加到文件尾.
	2.写入(Write)模式将覆盖文件的原有内容.

如果文件还不存在,任何一种模式都将创建文件.

'''
logfile = open("test.log", "w")
logfile.write("test succeeded")

logfile.close()

print(open('test.log').read())

logfile = open("test.log", 'a')
logfile.write("line 2")

logfile.close()
print(open("test.log").read())