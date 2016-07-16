'''

'''

class MyRange(object):
	def __init__(self, n):
		self.n = n
		self.num = 0

	def __iter__(self):
		return self
	
	def __next__(self):
		if self.num < self.n:
			result, self.num = self.num, self.num + 1
			return result
		else:
			raise StopIteration()	
	# def next(self):
	# 	if self.num < self.n:
	# 		result, self.num = self.num, self.num + 1
	# 		return result
	# 	else:
	# 		raise StopIteration()	

r = MyRange(3)
i = iter(r)
print(r == i) #True

print(next(r)) #0
print(next(i)) #1
print(next(i))
 print(next(i)) 会抛出StopIterator异常
# print(next(i))

for x in MyRange(3):
	print(x)