# IMPLEMENT A QUEUE SUCH THAT BOTH ENQUEUE AND DEQUEUE HAVE O(1) PERFORMANCE ON AVERAGE.

class FasterQueue:
	def __init__(self):
		self.items = []
		self.index = 0
	def enqueue(self, item):
		self.items.append(item)
	def dequeue(self):
		index = self.index
		self.index += 1
		return self.items[index]
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)

myQueue = FasterQueue()
myQueue.enqueue(3)
myQueue.enqueue(2)
myQueue.enqueue(6)
print(myQueue.dequeue())
myQueue.enqueue(2)
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
