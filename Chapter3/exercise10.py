# IMPLEMENT A RADIX SORTING MACHINE
from pythonds.basic.queue import Queue
def radix_sort(inputArr):
	digitBins = []
	for i in range(10):
		digitBins.append(Queue())
	mainBin = Queue()
	digitLength = None
	for element in inputArr:
		elementDigitLength = len(str(element))
		if not digitLength or elementDigitLength > digitLength:
			digitLength = elementDigitLength
	for element in inputArr:
		element = str(element)
		while len(element) < digitLength:
			element = "0" + element
		mainBin.enqueue(element)

	counter = 0
	while counter < digitLength:
		while not mainBin.isEmpty():
			element = mainBin.dequeue()
			digit = int(element[len(element)-1-counter])
			digitBins[digit].enqueue(element)
		for digitBin in digitBins:
			while not digitBin.isEmpty():
				element = digitBin.dequeue()
				mainBin.enqueue(element)
		counter += 1
	sortedArr = []
	while not mainBin.isEmpty():
		sortedArr.append(mainBin.dequeue())
	for i in range(len(sortedArr)):
		while sortedArr[i][0] == '0':
			sortedArr[i] = sortedArr[i][1:]
		sortedArr[i] = int(sortedArr[i])
	return sortedArr
print(radix_sort([25, 11, 91, 7]))
