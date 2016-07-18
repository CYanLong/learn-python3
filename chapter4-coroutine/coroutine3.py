

def coroutine(func):
	def start(*args, **kwargs):
		cr = func(*args, **kwargs)
		next(cr)
		return cr
	return start

@coroutine
def grep(pattern):
	print("Looking for %s" % pattern)
	while True:
		line = (yield) #yield None.
		if pattern in line:
			print(line)
