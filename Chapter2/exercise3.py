# DEVISE AN EXPEIRMENT THAT COMPARES THE PERFORMANCE OF THE DEL OPERATOR ON LISTS AND DICTIONARIES
import timeit
from random import randrange, choice
lstTimeArr = []
dTimeArr = []
for i in range(10000,1000001,20000):
	tx = timeit.Timer("del x[choice_x]", "from __main__ import x, choice_x")
	ty = timeit.Timer("del y[choice_y]", "from __main__ import y, choice_y")
	x = list(range(i))
	choice_x = randrange(len(x))
	lst_time = tx.timeit(number=1)
	y = {j:None for j in range(i)}
	choice_y = choice(list(y.keys()))
	d_time = ty.timeit(number=1)
	lstTimeArr.append(lst_time)
	dTimeArr.append(d_time)

for time in lstTimeArr:
	print(time)
print("###########################")
print("###########################")
for time in dTimeArr:
	print(time)
