#!/usr/bin/python

import sys
import getopt
import os
import ConfigParser
import fileinput

IndexFile = "mktags.files"
FileTypeList = ['.cpp', '.c','.py','.sh','.h','.hpp']
DirList = []
RootDir = "/Users/loc/projectsource/jabbber_10_5_trunk"
PrefixDirs = ['services', 'components', 'services', 'thirdparty/external', 'thirdparty/internal', 'tools']
Target = ''
DepFileList = ''
ImpDepFileList = '/Users/loc/projectsource/github/vi_ide_script/imp_deps.txt'
ContactServiceDepFileList = '/Users/loc/projectsource/github/vi_ide_script/contact_deps.txt'
PersonManagerDepFileList = '/Users/loc/projectsource/github/vi_ide_script/person_deps.txt'


def write_to_file(file, path):
	if len(FileTypeList) != 0:
		if not os.path.splitext(path)[1] in FileTypeList:
			return
	file.write(path + "\n")

def make_cscope():
	print "\nNow generating cscope database......"
	cmd = "cscope -bkq -i " + IndexFile
	os.system(cmd)
	print "Generate cscope database done!"

def make_tags():
	print "\nNow generating tags file......"	
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
	fileobj = open(IndexFile, "w")
	for path in DirList:
		for dirpath, dirnames, filenames in os.walk(path):
			for filename in filenames:
				write_to_file(fileobj, os.path.join(dirpath, filename))
	fileobj.close()

def add_target_dir():
	for prefixDir in PrefixDirs:
		wholepath = os.path.join(RootDir, prefixDir)
		targetDir = os.path.join(wholepath, Target)
		if os.path.exists(targetDir):
			DirList.append(targetDir)

def parse_args():
	if len(sys.argv) != 2:
		print "Please specify the target\n"

	global DepFileList
	global Target
	if sys.argv[1] == 'imp':
		Target = 'impresenceservices'
		DepFileList = ImpDepFileList
	elif sys.argv[1] == 'contact':
		Target = 'contactservice'
		DepFileList = ContactServiceDepFileList
	elif sys.argv[1] == 'person':
		Target = 'csf-person'
		DepFileList = PersonManagerDepFileList
	else:
		print "This target is currently not supported\n"
		
	add_dep_dir()
	add_target_dir()

def add_dep_dir():
	global DepFileList
	global Target
	for line in fileinput.input(DepFileList):
		if not line.strip():
			continue
		line = line[:-1]
		for prefixDir in PrefixDirs:
			wholepath = os.path.join(RootDir, prefixDir)
			depDir = os.path.join(wholepath, line)
			depDir = depDir[:-1]
			if os.path.exists(depDir):
				DirList.append(depDir)

if __name__ == "__main__":    

	refresh()

	parse_args()
	print DirList
	generate_index_file()

	make_cscope()
	make_tags()

