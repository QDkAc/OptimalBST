import random
def generate(n):
	return gen_traversal(0, n - 1)
def gen_traversal(l, r):
	if l >= r:
		return []
	m = random.randint(l, r - 1)
	ret = [m] 
	ret = ret + gen_traversal(l, m)
	ret = ret + gen_traversal(m + 1, r)
	return ret

