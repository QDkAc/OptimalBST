import random
import matplotlib.pyplot as plt

n = 100 #Length of Sequence
initial_tree_depth = 20

a = [] #Access Sequence

def gen_traversal(l, r, tl, tr):
	
        if l >= r:
                return
	if 1 == 1:
		plt.plot([l, r - 1], [tl, tl], color = "black");
		plt.plot([l, r - 1], [tr - 1, tr - 1], color = "black");
		plt.plot([l, l], [tl, tr - 1], color = "black");
		plt.plot([r - 1, r - 1], [tl, tr - 1], color = "black");
	m = random.randint(l, r - 1)
	if m >= (l + r) / 2:
		m = l
	else:
		m = r - 1
        a.append(m) 
        gen_traversal(l, m, tl + 1, tl + m - l + 1)
        gen_traversal(m + 1, r, tl + m - l + 1, tr)


gen_traversal(0, n, 0, n)

for i in range(len(a)): #Draw Access Points
        plt.plot([a[i]], [i], marker = "o", color= "r")

p = [] #Touch Points

for i in range(n): #Generate and Draw Initial Tree
        p.append((i, random.randint(-initial_tree_depth, -1)))
        plt.plot([p[i][0]], [p[i][1]], marker = "o", color = "g")

for i in range(n):
        cur = (a[i], i)
        p.append(cur)
        j = 0
        to_add = []
        while(j < len(p)):
                q = p[j]
                if cur[0] == q[0] or cur[1] == q[1]:
                        j = j + 1
                        continue
                ok = 0
                for r in p: #Checking Arborally Satisfication
                        if r != q and r != cur:
                                if r[0] >= min(cur[0], q[0]) and r[0] <= max(cur[0], q[0]):
                                        if r[1] >= min(cur[1], q[1]) and r[1] <= max(cur[1], q[1]):
                                                ok = 1
						break
                if ok == 0: # Not Satisfied
                        to_add.append((q[0], i))
                        plt.plot([q[0]], [i], marker = "o", color = "b")
                j = j + 1

        for point in to_add:
                p.append(point)


plt.axis([-1, n + 2, -1, n + 2])

plt.show()
