import random
def gen_traversal(o_file, l, r):
	if l >= r:
		return
	print l, r
	m = random.randint(l, r - 1)
	print >> o_file, m, 
	gen_traversal(o_file, l, m)
	gen_traversal(o_file, m + 1, r)

output_file = open("input.txt", "w")

gen_traversal(output_file, 0, 80)

output_file.close()
