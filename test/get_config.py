
FILE = "config.h"

def gconfig():
	global FILE
	
	fp = open(FILE,'r')
	lines = fp.readlines()
	
	ll = list()
	for line in lines:
		data = line.strip()
		if data.startswith("#define N "):
			ll.append(int(data.split(" ")[2]))
		elif data.startswith("#define D "):
			ll.append(int(data.split(" ")[2]))
		elif data.startswith("#define PSIZE "):
			ll.append(int(data.split(" ")[2]))
		elif data.startswith("#define Distr "):
			ll.append(data.split(" ")[2][1])
	
	fp.close()
	return ll