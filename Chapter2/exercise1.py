# DEVISE AN EXPERIMENT TO VERIFY THAT THE LIST INDEX OPERATOR IS O(1)
import timeit
import random
obj = timeit.Timer("random.choice(x)",
                       "from __main__ import x, random")

for i in range(1000, 10000, 1000):
	x = list(range(i));
	print(x[0], x[-1])
	print(str(obj.timeit(number=1000)) + " milliseconds")