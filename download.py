# -*- coding: utf-8 -*-  
import os

level = 8

website = 'http://las.com/'
dataset = 'test/'
data = website + dataset + 'data/'
hierarchy = website + dataset + 'hierarchy/'

cmd_curl = 'curl -o '
cmd_wget = 'wget '
ext = '.bat'

dataRoot = 'F:/laz_data/'
jsonRoot = 'F:/laz_json/'
download = dataRoot + dataset
downloadjson = jsonRoot + dataset

if not os.path.exists(dataRoot):
	os.mkdir(dataRoot)
if not os.path.exists(jsonRoot):
	os.mkdir(jsonRoot)
if not os.path.exists(download):
	os.mkdir(download)
if not os.path.exists(downloadjson):
	os.mkdir(downloadjson)

for lvl in range(level):
	print lvl
	fl = open(download + str(lvl + 1) + ext, 'a')
	fj = open(downloadjson + str(lvl + 1) + ext, 'a')
	num = 2 << lvl
	
	# laz dir
	save_dir = download + str(lvl + 1) + '/'
	if not os.path.exists(save_dir):
		os.mkdir(save_dir)

	# json dir
	save_dir_json = downloadjson + str(lvl + 1) + '/'
	if not os.path.exists(save_dir_json):
		os.mkdir(save_dir_json)

	for x in range(num):
		for y in range(num):
			for z in range(num):
				# laz
				fname = str(lvl + 1) + '-' + str(x) + '-' + str(y) + '-' + str(z) + '.laz'
				save_path = save_dir + fname
				link = data + fname
				laz = cmd_curl + save_path + ' ' + link + '\n'

				# json
				fname = str(lvl + 1) + '-' + str(x) + '-' + str(y) + '-' + str(z) + '.json'
				save_path = save_dir_json + fname
				link = hierarchy + fname
				json = cmd_curl + save_path + ' ' + link + '\n'

				fl.write(laz)
				fj.write(json)
	fl.close()
	fj.close()

