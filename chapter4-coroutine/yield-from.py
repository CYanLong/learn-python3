def reader():
	for i in range(4):
		yield '<< %s' % i

def reader_wrapper(g):
	for v in g:
		yield v

g = reader() #g is a generator
wrap = reader_wrapper(g)
for i in wrap:
	print(i)

print("-----")

#通过 yield from 可以代替手动迭代生成器
def reader_wrapper2(g):
	yield from g

g = reader()
wrap2 = reader_wrapper2(g)
for i in wrap2:
	print(i)


print("-----")
def write():
	while True:
		w = (yield)
		print('>>', w)


def write_wrapper(coro):
	coro.send(None) #prime the coro
	while True:
		try:
			x = (yield)
			coro.send(x)
		except StopIteration:
			pass

def write_wrapper2(coro):
	yield from coro

w = write() # a generator
wrap = write_wrapper(w) 
wrap.send(None) # "prime" the coroutine
for i in range(4):
	wrap.send(i)

