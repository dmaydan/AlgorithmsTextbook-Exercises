# USING BinaryHeap CLASS, IMPLEMENT A NEW PriorityQueue CLASS TO IMPLEMENT THE CONSTRUCTOR AND THE ENQUEUE AND DEQUEUE METHODS.
# I AM IMPLEMENTING THE PRIORITY QUEUE WITH A MIN HEAP SO THAT THE SMALLEST ITEM WILL BE AT THE FRONT
class PriorityQueue:
	def __init__(self):
		self.bh = BinHeap()
	def enqueue(self, item):
		self.bh.insert(item)
	def dequeue(self):
		return self.bh.delMin()
class BinHeap:
	def __init__(self):
			self.heapList = [0]
			self.currentSize = 0
	
	def percUp(self,i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				 tmp = self.heapList[i // 2]
				 self.heapList[i // 2] = self.heapList[i]
				 self.heapList[i] = tmp
			i = i // 2
				
	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percDown(self,i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
					tmp = self.heapList[i]
					self.heapList[i] = self.heapList[mc]
					self.heapList[mc] = tmp
			i = mc

	def minChild(self,i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1
				
	def delMin(self):
		try:
			retval = self.heapList[1]
			self.heapList[1] = self.heapList[self.currentSize]
			self.currentSize = self.currentSize - 1
			self.heapList.pop()
			self.percDown(1)
			return retval
		except:
			return None

	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1
pq = PriorityQueue()
pq.enqueue(9)
pq.enqueue(5)
pq.enqueue(6)
pq.enqueue(2)
pq.enqueue(3)

print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())


