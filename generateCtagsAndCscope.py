#!/usr/bin/python

import sys
import getopt
import os
import ConfigParser
import fileinput

IndexFile = "mktags.files"
FileTypeList = ['.cpp', '.c','.py','.sh','.h','.hpp','.java']
DirList = []
RootDir = "/home/luocheng/tvosproject"
#PrefixDirs = ['services', 'components', 'services', 'thirdparty/external', 'thirdparty/internal', 'tools', 'products']
PrefixDirs = []
Target = ''
DepFileList = ''
GameStoreFileList = '/home/luocheng/mygit/vi_ide_script/GameStore_deps.txt'
EnjoyCenterFileList = '/home/luocheng/mygit/vi_ide_script/EnjoyCenter_deps.txt'
TestFileList = '/home/luocheng/mygit/vi_ide_script/Test_deps.txt'


def write_to_file(file, path):
	if len(FileTypeList) != 0:
		if not os.path.splitext(path)[1] in FileTypeList:
			return
	file.write(path + "\n")

def make_cscope():
	print "\nNow generating cscope database......"
        cmd = "cscope -bkqR -i " + IndexFile
	#if GenerateLocally:
		#print "local path: " + os.getcwd()
		#cmd = "cscope -Rbq"
	#else:
		#cmd = "cscope -bkqR -i " + IndexFile
	os.system(cmd)
	print "Generate cscope database done!"

def make_tags():
	print "\nNow generating tags file......"	
	if GenerateLocally:
		cmd = "ctags --c++-kinds=+p --fields=+iaS --extra=+q -R " + os.getcwd()
	else:
		cmd = "ctags --c++-kinds=+p --fields=+iaS --extra=+q -L " + IndexFile
	os.system(cmd)
	print "Generate tags file done!"	

def refresh():
	print "\nClean obsolete files ...."
	cmd = "rm cscope* -f"
	os.system(cmd)
	cmd = "rm tags -f"
	os.system(cmd)
	cmd = "rm mktags.files -f"
	os.system(cmd)

def generate_index_file():
	#if GenerateLocally:
		#return 0
	fileobj = open(IndexFile, "w")
	for path in DirList:
		for dirpath, dirnames, filenames in os.walk(path):
			for filename in filenames:
				write_to_file(fileobj, os.path.join(dirpath, filename))
	fileobj.close()

def add_target_dir():
	if GenerateLocally:
		return 0
        if not PrefixDirs:
            targetDir = os.path.join(RootDir, Target)
            if os.path.exists(targetDir):
                DirList.append(targetDir)
	for prefixDir in PrefixDirs:
		wholepath = os.path.join(RootDir, prefixDir)
		targetDir = os.path.join(wholepath, Target)
		if os.path.exists(targetDir):
			DirList.append(targetDir)

def parse_args():
	if len(sys.argv) != 2:
		print "Please specify the target\n"
		sys.exit(-2)

	global DepFileList
	global Target
	global GenerateLocally 
	GenerateLocally = 0
        if sys.argv[1] == 'gamestore':
                Target = 'GameStore'
                DepFileList = GameStoreFileList
        elif sys.argv[1] == 'enjoy':
                Target = 'EnjoyCenter'
                DepFileList = EnjoyCenterFileList
        elif sys.argv[1] == 'ui':
                Target = 'tvosuilibs'
                DepFileList = TestFileList
	elif sys.argv[1] == 'local':
		GenerateLocally = 1
	else:
		Target = sys.argv[1]
		#print "This target is currently not supported\n"
		#sys.exit(-2)
		
	if DepFileList != '':
		add_dep_dir()
        if GenerateLocally:
                add_local_dir()
	add_target_dir()

def add_local_dir():
        if not GenerateLocally:
                return 0;
        DirList.append(os.getcwd());

def add_dep_dir():
	global DepFileList
	global Target
	if GenerateLocally:
		return 0
	for line in fileinput.input(DepFileList):
		if not line.strip():
			continue
		line = line[:-1]
                if not PrefixDirs:
                    depDir = os.path.join(RootDir, line)
                    if os.path.exists(depDir):
                        DirList.append(depDir)
                    print depDir
		for prefixDir in PrefixDirs:
			wholepath = os.path.join(RootDir, prefixDir)
			depDir = os.path.join(wholepath, line)
			depDir = depDir[:-1]
			if os.path.exists(depDir):
				DirList.append(depDir)

if __name__ == "__main__":    

	refresh()

	parse_args()
	generate_index_file()

	make_cscope()
	make_tags()

