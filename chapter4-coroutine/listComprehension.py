'''
List Comprehensions(列表解析)：list comprehensions用来方便的，简单的构造list。
'''

# 常规的创建list的方式
squares = []
for x in range(10):
	squares.append(x**2) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(squares)

squares = list(map(lambda x : x**2, range(10)))

squares = [x**2 for x in range(10)]