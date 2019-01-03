# IMPLEMENT THE QUEUE ADT, USING A LIST SUCH THAT THE REAR OF THE QUEUE IS AT THE END OOF THE LIST

class Queue:
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.append(item)
	def dequeue(self, item):
		return self.items.pop(0)
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)