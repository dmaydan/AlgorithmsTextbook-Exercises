# MODIFY THE HOT POTATO SIMULATION TO ALLOW FOR A RANDOMLY CHOSEN COUNTING VALUE SO THAT EACH PASS IS NOT PREDICTABLE FROM THE PREVIOUS ONE
from pythonds.basic.queue import Queue
import random
def hotPotato(namelist):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		num = random.randrange(1, len(namelist))
		print(num)
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())

		simqueue.dequeue()

	return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"]))