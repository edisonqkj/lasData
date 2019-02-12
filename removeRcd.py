import os

file = 'F:/laz_data/iowa-bridge/8.bat'
# target = 'curl -o F:/laz_data/8/8-41-77-58.laz http://na-c.entwine.io/nyc/ept-data/8-41-77-58.laz\n'
target = 'curl -o F:/laz_data/iowa-bridge/8/8-39-191-47.laz http://na-c.entwine.io/iowa-bridge/ept-data/8-39-191-47.laz\n'
fname,fext = os.path.splitext(file)
out = fname + '_left' + fext

read = open(file, 'r')
write = open(out, 'w')
line =  read.readline()

find = False
while line:
	# print line
	if line == target:
		find = True
	else:
		if find:
			write.write(line)
	line = read.readline()

read.close()
write.close()