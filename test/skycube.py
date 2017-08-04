from get_config import gconfig
from skydata import genData
from get_data import gdata

from time import time

Nidx = 0
Didx = 1
DistrIdx = 2
PszIdx = 3

#
cc = gconfig()
print "N:",cc[Nidx],",D:",cc[Didx],",Distr:",cc[DistrIdx],",PSIZE:",cc[PszIdx]

tt = time()
fname = genData(cc[Nidx],cc[Didx],str(cc[DistrIdx]))
tt = time() - tt
print "Generate data elapsed time:",tt

tt = time()
points = gdata(fname,22*cc[Didx])
tt = time() - tt
print "Read elapsed time:",tt

def second_smallest(numbers):
	m1,m2 = float(1024*1024), float(1024*1024)
	for x in numbers:
		if x <=m1:
			m1,m2=x,m1
		elif x < m2:
			m2 = x
	return m2
	
print second_smallest([2,3,3,4])

