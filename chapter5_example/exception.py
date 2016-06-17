'''
对比两种打开方式,第一种直接打开,如果文件不存在,引发IOError异常,会终止程序.
第二种使用try... except IOError 机制,当出现异常时,我们可以自己控制程序走向,可以记录下错误,并继续执行,程序可以不终止.
'''

#fsock = open("/notthere", "r")

try:
	fsock = open("/notthere")
except IOError:
	print("The file does not exist, exiting gracefully")
print("This line will always print")
