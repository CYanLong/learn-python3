# bitch_file_rename.py
# Created: 12th July 2016
'''
改变指定目录下特定后缀名的文件。
'''

__author__ = 'Yanlong Chen'
__version__ = '1.0'

import osc
import sys

def batch_rename(work_dir, old_ext, new_ext):
	for filename in os.listdir(work_dir):
		file_ext = os.path.splitext(filename)[1] #得到文件后缀名
		if old_ext == file_ext:
			newfile = filename.replace(old_ext, new_ext)
			os.rename(
				os.path.join(work_dir, filename),
				os.path.join(work_dir, newfile)
			)

def main():
	work_dir = 'work-dir'
	old_ext = '.txt'
	new_ext = '.py'
	batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
	print("sss")
	main()

		