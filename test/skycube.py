from get_config import gconfig
from skydata import genData
from get_data import gdata

from time import time

Nidx = 0
Didx = 1
DistrIdx = 2
PszIdx = 3

cc = gconfig()

print "N:",cc[Nidx],",D:",cc[Didx],",Distr:",cc[DistrIdx],",PSIZE:",cc[PszIdx]
fname = genData(cc[Nidx],cc[Didx],str(cc[DistrIdx]))

tt = time()
points = gdata(fname,22*cc[Didx])
tt = time() - tt
print "Read elapsed time:",tt

#print points[0]



