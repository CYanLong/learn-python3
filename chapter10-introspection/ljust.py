'''
ljust是一个字符串方法.
ljust用空格填充字符串以符合指定的长度. 
'''
if __name__ == '__main__':
	s = "buildConnectionString"
	print(s.ljust(30) + "_end") #buildConnectionString         _end
	print(s.ljust(20) + "_end") #buildConnectionString_end
