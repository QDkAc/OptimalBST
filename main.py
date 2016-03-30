import matplotlib.pyplot as plt
import random
import sequential
import greedyASS
import path
import traversal
import splay

n = 50
access_sequence = path.generate(n)
#n = 10
#access_sequence = [7, 0, 6, 3, 5, 2, 9, 8, 1, 4]
algorithm = splay.Splay(range(n))

for i in range(len(access_sequence)):
	touch_points = algorithm.access(access_sequence[i])
	plt.plot(access_sequence[i], [i], marker = "o", color = "r")
	for p in touch_points:
		if p != access_sequence[i]:	
			plt.plot([p], [i], marker = "o", color = "b")

plt.axis([-1, n + 2, -1, n + 2])
plt.show()

