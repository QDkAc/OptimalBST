import matplotlib.pyplot as plt
import random
input_file = open("input.txt", "r")
s = input_file.readline().strip()
a = map(int, s.split())

n = len(a)

for i in range(len(a)):
	print(a[i], i)
	plt.plot([a[i]], [i], marker = "o", color= "r")
p = []
for i in range(100):
	p.append((random.randint(0, n - 1), random.randint(-10, -1)))
	plt.plot([p[i][0]], [p[i][1]], marker = "o", color = "g")
for i in range(len(a)):
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
		for r in p:
			if r != q and r != cur:
				if r[0] >= min(cur[0], q[0]) and r[0] <= max(cur[0], q[0]):
					if r[1] >= min(cur[1], q[1]) and r[1] <= max(cur[1], q[1]):
						ok = 1
		if ok == 0:
			to_add.append((q[0], i))
			plt.plot([q[0]], [i], marker = "o", color = "b")
			print(q[0], i)
		j = j + 1
	for point in to_add:
		p.append(point)

plt.plot([0, 1], [0, 1])
plt.axis([-1, n + 2, -1, n + 2])
plt.show()

