from get_config import gconfig
from skydata import genData
from get_data import gdata

from mfunc import fsum, fmin_sum, min_fsum
from sfs import sfs

from time import time

def init():
	tt = time()
	fname = genData(cc[Nidx],cc[Didx],str(cc[DistrIdx]))
	tt = time() - tt
	print "Generate data elapsed time:",tt

	tt = time()
	points = gdata(fname,22*cc[Didx])
	tt = time() - tt
	print "Read elapsed time:",tt
	return points

Nidx = 0
Didx = 1
DistrIdx = 2
PszIdx = 3

#
cc = gconfig()
print "N:",cc[Nidx],",D:",cc[Didx],",Distr:",cc[DistrIdx],",PSIZE:",cc[PszIdx]
points = init()

sfs(points,fmin_sum(points))
