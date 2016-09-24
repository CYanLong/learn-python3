import asyncio
import threading


@asyncio.coroutine
def hello():
	print("Hello world! (%s)" % threading.currentThread())
	yield from asyncio.sleep(1) #yield from 语法用来方便调用另一个协程
	print("hello again! (%s)" % threading.currentThread())

#loop = asyncio.get_event_loop()
#将hello协程添加到循环队列中
#tasks = [hello(), hello()]
#loop.run_until_complete(asyncio.wait(tasks))
#loop.close()

import datetime

async def display_data(loop, name):
	end_time = loop.time() + 5.0
	print("end_time %s (%s) in thread (%s)" % (end_time, name, threading.currentThread()))
	while True:
		print("now: %s (%s) in thread (%s)" % (datetime.datetime.now(), name, threading.currentThread()))
		if (loop.time() + 1.0) >= end_time:
			break
		await asyncio.sleep(1)
print("============")
loop2 = asyncio.get_event_loop()
d1 = display_data(loop2, "task1")
d2 = display_data(loop2, "task2")
tasks = [d1, d2]
loop2.run_until_complete(asyncio.wait(tasks))
loop2.close()

