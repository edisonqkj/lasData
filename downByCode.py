# -*- coding: utf-8 -*-  
import os

import requests 
import urllib
import urllib2
import datetime

def getfiles(path, files):
	#传入存储的list
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		if not os.path.isdir(file_path):
			files.append(file_path)


print "Start downloading......"
data_dir = 'f:/laz_data/'
files = []
getfiles(data_dir, files)

bats = []
for file in files:
	fname,fext = os.path.splitext(file)
	if fext == '.bat':
		bats.append(file)
# print bats

bats = ['F:/laz_data/9.bat']
ok = False
for bat in bats:
	print bat
	file = os.path.basename(bat)
	fname = file.split('.')[0]
	with open(bat, 'r') as read:
		num = 1
		line = read.readline()
		while line:
			if num % 5 == 0:
				# log.flush()
				print num
			strs = line.split(' ')
			save_laz = strs[2]
			url = strs[3]

			t = str(datetime.datetime.now())
			log = open(data_dir + 'log' + fname + '.txt','a')
			log.write('Start: ' + t + '   ' + url)
			log.close()

			urllib.urlretrieve(url, save_laz)

			# r = requests.get(url) 
			# with open(save_laz, "wb") as code:
			# 	code.write(r.content)

			# f = urllib2.urlopen(url) 
			# data = f.read() 
			# with open(save_laz, "wb") as code: 
			# 	code.write(data)

			line = read.readline()





