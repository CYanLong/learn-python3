# create_dir_if_not_there.py
# Created:12th July 2016

'''
'''

__author__ = "Yanlong Chen"
__version__ = '1.0'

import os

def create_dir(work_dir, new_dir):
	for filename in os.listdir(work_dir):
		if filename == new_dir:
			print('工作路径已存在 %s 目录' % new_dir)
			return 

	os.makedirs(new_dir)

def create_dir2(work_dir, new_dir):
	if not os.path.exists(work_dir + '/' + new_dir):
		os.makedirs(work_dir + '/' + new_dir)

if __name__ == '__main__':
	create_dir("work-dir", "new_dir")


