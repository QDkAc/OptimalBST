#Without initial tree

class greedyASS:
	def __init__(self, n):
		self.n = n
		self.m = 0
		self.mra = [-1] * n
	def access(self, key):
		to_add = [key]
		for i in xrange(self.n):
			if (i == key or self.mra[i] == -1):
				continue
			ok = 0
			for j in xrange(min(i, key), max(i, key) + 1):
				if self.mra[j] >= self.mra[i] and j != i:
					ok = 1
					break
			if ok == 0:
				to_add.append(i)
		for x in to_add:
			self.mra[x] = self.m
		self.m = self.m + 1
		return to_add
