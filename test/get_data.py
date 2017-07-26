import os

def gdata(fname,lineSZ):
	fp = open(fname,'r')
	points = list()
	
	buffer= lineSZ*32*1024
	data = fp.read(buffer)
	while len(data) > 0:
		lines = data.split("\n")
		for line in data.strip().split("\n"):
			#print line
			p = [ float(v) for v in line.strip().split(",") ]
			#print p
			points.append(p)
		data = fp.read(buffer)
	
	fp.close()
	os.remove(fname)
	return points