import os
#os.path.join将多个路径连在一起.
print(os.path.join("music\_single", "Sugar.mp3"))

#os.path.split()函数对全路径名进行分割,返回一个包含路径和文件名的tuple.
(filepath, filename) = os.path.split("c:\Sugar.mp3")
print("%s %s" % (filepath, filename))

#os.path.splitext对文件名进行分割,并且返回一个包含了文件名
#和文件扩展名的tuple.
(shortname, extension) = os.path.splitext("Sugar.mp3")
print("%s %s" % (shortname, extension))

#listdir函数接收一个路径名,并返回那个目录的内容的list.
os.listdir("music/_single")