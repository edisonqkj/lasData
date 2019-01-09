# -*- coding: utf-8 -*-  
import os,shutil


def getdirs(path, dirs):
	#传入存储的list
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		if os.path.isdir(file_path):
			dirs.append(file_path)

def getfiles(path, files):
	#传入存储的list
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		if not os.path.isdir(file_path):
			files.append(file_path)

data_dir = 'f:/laz_data/'
fail_dir = 'f:/laz_data/fail'
file_error = []
dirs = []
getdirs(data_dir, dirs)

for i in range(len(dirs)):
	if dirs[i] == fail_dir:
		continue
	print dirs[i]

	files = []
	getfiles(dirs[i], files)
	# print len(files)
	for j in range(len(files)):
		fname,fext = os.path.splitext(files[j])
		if fext == '.laz':
			read = open(files[j], 'r')
			start_str = read.read(3)
			read.close()

			if start_str != 'LAS':
				file_error.append(files[j])
				# print start_str
			# size = os.path.getsize(files[j])
			# if size <= 243:
			# 	file_error.append(files[j])

print len(file_error)
file_error = map(lambda x: x.replace('\\','/') + '\n', file_error)
with open(data_dir + 'error.txt', 'w') as f:
	f.writelines(file_error)

if not os.path.exists(fail_dir):
	os.mkdir(fail_dir)

for i in range(len(file_error)):
	target = fail_dir + '/'
	# shutil.move(file_error[i], fail_dir)


