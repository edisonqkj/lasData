# -*- coding: utf-8 -*-  
import os

import requests 
import urllib
import urllib2
import datetime

satId = 25544
locNum = 1
# https://www.n2yo.com/sat/instant-tracking.php?s=25544&hlat=30.29365&hlng=120.16142&d=1000&r=806464686839.7404&tz=GMT+08:00&O=n2yocom&rnd_str=f5425b93471dc5eab18838dd9f238558&callback=
# "d":"19.70138939|-157.99489549|313.52|-74.97|15.80835123|10.20621074|408.68|0|25544|1550629279|0||||"
url = 'https://www.n2yo.com/sat/instant-tracking.php?s=' + str(satId) + '&d=' + str(locNum)
print url
file1 = 'loc1.txt'
file2 = 'loc2.txt'
file3 = 'loc3.txt'

# urllib.urlretrieve(url, file1)

r = requests.get(url)
print r.content
# with open(file2, "wb") as code:
# 	code.write(r.content)

# f = urllib2.urlopen(url) 
# data = f.read() 
# with open(file3, "wb") as code: 
# 	code.write(data)