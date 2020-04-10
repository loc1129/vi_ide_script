#coding:utf-8
#please refer to https://blog.csdn.net/langzxz/article/details/77895178
#step1 : 安装tinify模块 sudo pip install --upgrade tinify
#step2: 去https://tinypng.com/developers获取api key, 每个月免费压缩500张
#已经获取的api key
#luocheng@qiyi.com： KRMywcK55DBhjlKNgcdKgGKgc7ZgnCvB
#loc1129@163.com: 
#临时邮箱：36MZPVzfHDcljNT6QCHy7FKbGFwDQLTP
#临时邮箱：x3ww3tLHzh4p9prhK37hwVjRkc9xt9wr
#/usr/bin/python
 
import os
import sys
import os.path
import shutil
import tinify
 
temPath = os.getcwd()+'/'+'temDir'			# 临时目录,注意该脚本最后是要删掉这个临时目录的
tinify.key = "x3ww3tLHzh4p9prhK37hwVjRkc9xt9wr"		# 刚刚申请的API KEY
#tinify.key = "U54uo4N330OaU_85vEgHv63djEf2es"		# 刚刚申请的API KEY
version = "0.0.1"				# 版本
 
# 压缩的核心
def compress_core(inputFile, outputFile, img_width):
    try:
	source = tinify.from_file(inputFile)
	if img_width is not -1:
		resized = source.resize(method = "scale", width  = img_width)
		resized.to_file(outputFile)
	else:
		source.to_file(outputFile)
        return 0
    except tinify.AccountError, e:
        print "the error msg is: %s" %e.message
        return 1
    except tinify.ClientError, e:
        print "the error msg is: %s" %e.message
        return 1
    except tinify.ServerError, e:
        print "the error msg is: %s" %e.message
        return 1
    except tinify.ConnectionError, e:
        print "the error msg is: %s" %e.message
        return 1
    except Exception, e:
        print "the error msg is: %s" %e.message
        return 1


 
# 压缩一个文件夹下的图片
def compress_path(path, width):
    print "compress_path-------------------------------------"
    fromFilePath = path 			# 源路径
    print "fromFilePath=%s" %fromFilePath
    compress_ret = 0
 
    for root, dirs, files in os.walk(fromFilePath):
#        print "root = %s" %root
#        print "dirs = %s" %dirs
#        print "files= %s" %files
        if compress_ret is not 0:
            break
        for name in files:
            fileName, fileSuffix = os.path.splitext(name)
            if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
                fromfile =  os.path.join(root,name)
                tofile = os.path.join(temPath,name)
                picsize = os.path.getsize(fromfile)
                if picsize >= 10240:
                    print fromfile
                    print "origin size is %s" %picsize
                    compress_ret = compress_core(fromfile, tofile, width)

                    if compress_ret is not 0:
                        print "fail to compress %s" %fromfile 
                        break

                    compresssize = os.path.getsize(tofile)
                    print "compress size is %s" %compresssize 
                    shutil.copy2(tofile, fromfile)# 将压缩后的文件覆盖原文件
 
 
 
if __name__ == "__main__":
    if not os.path.exists(temPath):
        os.mkdir(temPath)
    if len(sys.argv)==2:
        compress_path(sys.argv[1],-1)
    if len(sys.argv)==3:
        compress_path(sys.argv[1],sys.argv[2])
    shutil.rmtree(temPath)
