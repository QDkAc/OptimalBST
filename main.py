import matplotlib.pyplot as plt
import random
import sequential
import greedyASS

n = 100
access_sequence = sequential.generate(n)
algorithm = testBST.testBST(n)

for i in xrange(len(access_sequence)):
	touch_points = algorithm.access(access_sequence[i])
	plt.plot(access_sequence[i], [i], marker = "o", color = "r")
	for p in touch_points:
		if p != access_sequence[i]:	
			plt.plot([p], [i], marker = "o", color = "b")

plt.show()

