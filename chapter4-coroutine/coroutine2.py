'''
A coroutine might run indefinitely
Use .close() to shut it down.
'''
def grep(pattern):
	print("Looking for %s" % pattern)
	while True:
		line = (yield) #yield None.
		if pattern in line:
			print(line)

g = grep("python") #When you call a coroutine, nothing happens.
print(next(g)) # None
		#They only run in response to next() and send() methods
		#On first operation, coroutine starts running.
		#All coroutines must be "Primed" by first next()(or send(Node))
		#This advances execution to the location of the first yield expression
		#At this point, it's ready to receive a value.
g.send("Yeah, but no, but yeah, but no")
g.send("A series of tubes")
g.send("python generators rock!")



