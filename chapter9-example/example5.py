'''
此例子根据传入的目录(dictionary)和后缀名(extName)得到文件的相关信息.
信息的获取由专门的类来实现.若没有为此文件专门写特定的信息解析类,则使用
FileInfo基类获取最基本的文件名信息.

在这里,存在三个类, UserDict, FileInfo, MP3FileInfo

UserDict:几乎原样封装了一个dict对象.(属性名为data)
FileInfo(UserDict):
	获取文件信息的基类.继承了UserDict.在此类实例化时会初始化
	name=filename的信息.(存入父类的dict对象中)如果在创建此对象时
	没有提供filename,则name = None.


MP3FileInfo(FileInfo):
	用来专门处理MP3文件的类.继承自FileInfo.
	当创建此对象时,会调用父类(FileInfo)的__init__方法.
	但当初始化方法调用self["name"]时会调用__setitem__方法，
	MP3FileInfo覆盖了此方法,并不是单纯的将name = filename
	存入dict对象中,而是做了针对性的parse.

'''
import os
import sys
from UserDict import UserDict

def stripnulls(data):
	return data.replace("\00", "").strip()

class FileInfo(UserDict):
	''''''
	def __init__(self, filename = None):
		UserDict.__init__(self)
		#将引发__setitem__的调用,可能会调用到子类的覆盖方法.
		self["name"] = filename 


class MP3FileInfo(FileInfo):

	tagDataMap = {"title" : (3, 33, stripnulls),
				"artist": (33, 63, stripnulls),
				"album": (63, 93, stripnulls),
				"year": (93, 97, stripnulls),
				"comment": (97, 126, stripnulls),
				"genre": (127, 128, ord)} 

	#文件对象的seek方法在被打开文件中移动到另一个位置.
	#
	def __parse(self, filename):
		self.clear()
		try:
			fsock = open(filename, "rb", 0)
			print(fsock.tell())
			try:
				fsock.seek(-128, 2)
				tagdata = fsock.read(128)
			finally:
				fsock.close()
			if tagdata[:3] == "TAG": 
				for tag, (start, end, parseFunc) in self.tagDataMap.items():
					self[tag] = parseFunc(tagdata[start:end])
		except IOError:
			pass


	def __setitem__(self, key, item):
		#如果给name关键字赋值,我们还需要做一些额外的事情.
		#print("mp3 class: key = %s ; value = %s" % (key, item))
		if key == "name" and item:
			self.__parse(item)

		FileInfo.__setitem__(self, key, item)


#1、os.path是一个模块的引用.
#2、os.listdir函数接受一个路径名,并返回那个目录的内容的list.
#3、os.path.normcase根据操作系统的缺省值对大小写进行标准化处理.
#例如,在window下,normcase将把整个文件名转化为小写字母.
#而在UNIX下,它将返回未做修改的文件名.
#4、os.path.splitext函数可以用来对文件名进行分割,并且返回
#包含了文件名和文件拓展名的tuple.
#5、os.path.join函数把一个或多个部分路径名连接成一个.
def listDirectory(directory, fileExtList):

	fileList = [os.path.normcase(f)
				for f in os.listdir(directory)]

	#得到所有fileExtList后缀名的路径.
	fileList = [os.path.join(directory, f)
				for f in fileList
				if os.path.splitext(f)[1] in fileExtList]

	#1、sys.modules是一个dict,它包含程序导入过的所有模块.
	#key=模块名,value=模块对象.
	#2、每个python类都拥有一个类属性__module__,它定义了这个类的模块的名字.
	#将它与sys.modules dict复合使用,可以得到定义了某个类的模块的引用.
	#3、os.path.splitext(filename)[1].upper()[1:] 得到文件的扩展名,并将其转换为大写字母,从圆点处进行分片.
	#4、在生成处理类名之后,我们查阅这个模块中是否存在这个类,如果存在,返回;否则,返回基类FileInfo.
	#要注意的是,这个函数返回的是一个类,而不是类的实例.类本身.

	def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
		subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:] #
		return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
	#getFileInfoClass(f)得到一个的类,并通过(f)调用此类来创建对象.
	return [getFileInfoClass(f)(f) for f in fileList]


if __name__ == "__main__":
	for info in listDirectory("music/_singles", [".mp3"]):
		print("\n".join(["%s=%s" % (k, v) for k, v in info.items()]))
