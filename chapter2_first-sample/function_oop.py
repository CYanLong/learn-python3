'''
2.3:万物皆对象.
Python函数有属性,并且这些属性在运行时是可用的.
在Python中,函数同其他东西一样也是对象.

下面例子通过访问外部模块中的函数的__doc__属性得到函数的说明文档

'''

import sys
import example2

if __name__ == '__main__':
	print(sys.path)
	print(example2.buildConnectionString.__doc__)


