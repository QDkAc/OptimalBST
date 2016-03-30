import random
def generate(n):
	l = 0
	r = n - 1
	ret = []
	while l <= r:
		if (random.randint(0, 1) == 0):
			ret.append(l)
			l = l + 1
		else:
			ret.append(r)
			r = r - 1
	return ret

	
