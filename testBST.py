class testBST:
	def __init__(self, n):
		self.n = n
	def access(self, x):
		ret = [x]
		if x > 0:
			ret.append(0)
		if x < self.n - 1:
			ret.append(x + 1)
		return ret
