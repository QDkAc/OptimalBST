class Splay:
	
	root = None
	node = {}
	
	def __init__(self,pre):
		self.key = pre[0];
		Splay.node[pre[0]] = self
		self.c = [None, None]
		self.p = None
		left = [x for x in pre if x<self.key]
		right = [x for x in pre if x>self.key]
		if len(left) > 0:
			self.c[0] = Splay(left)
			self.c[0].p = self
		if len(right) > 0:
			self.c[1] = Splay(right)
			self.c[1].p = self
		Splay.root = self
	
	def rotate(self,k):
		p = self.p
		p.c[k] = self.c[~k]
		if (p.c[k] != None):
			p.c[k].p = p
		self.p = p.p
		if (self.p != None):
			self.p.c[self.p.c[1] == p] = self
		self.c[~k] = p
		p.p = self
	
	def splay(node,top):
		aim = top.p
		step = [node.key]
		while node.p != aim:
			if node.p == top:
				node.rotate(top.c[1] == node)
				step.append(top.key)
				continue
			p = node.p
			pp = node.p.p
			step.append(p.key)
			step.append(pp.key)
			flag = (pp.c[1] == p)
			if (p.c[flag] == node):
				p.rotate(flag)
				node.rotate(flag)
			else:
				node.rotate(~flag)
				node.rotate(flag)
		if aim == None:
			Splay.root = node
		return step
	
	def access(self, key):
		return Splay.splay(Splay.node[key], Splay.root)
