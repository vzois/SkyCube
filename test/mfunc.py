
def fsum(points):
	rank = list()
	for p in points:
		rank.append(sum(p))
	
	return rank

def fmin_sum(points):
	rank = list()
	for p in points:
		rank.append([min(p),sum(p)])
	return rank

def ssmall(numbers):
	m1,m2 = float(1024*1024), float(1024*1024)
	for x in numbers:
		if x <=m1:
			m1,m2=x,m1
		elif x < m2:
			m2 = x
	return m2

def min_fsum(points):
	rank = list()
	for p in points:
		m1 = min(p)
		m2 = ssmall(p)
		rank.append(m1+m2)
	return rank
		

