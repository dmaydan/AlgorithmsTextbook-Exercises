# IMPLEMENT A DEQUE USING LINKED LISTS
class Deque:
	def __init__(self):
		# Head of linked list is rear/tail is front
		self.contents = UnorderedList()
	def removeFront(self):
		return self.contents.pop()
    def removeFront(self):
        return self.contents.pop(0)
    def addFront(self, item):
        return self.contents.append(item)
    def addFront(self, item):
        return self.contents.add(item)
	def dequeue(self):
		return self.contents.pop()
	def isEmpty(self):
		return self.contents.length() == 0
	def size(self):
		return self.contents.size()

class Node:

    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length += 1

    def length(self):
        return self.length

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current != None:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            self.length -= 1
    def __str__(self):
        current = self.head
        outputList = []
        while current != None:
            outputList.append(current.getData())
            current = current.getNext()
        return str(outputList)
    def append(self, item):
        temp = Node(item)
        current = self.head
        if current == None:
            self.head = temp
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.length += 1
    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = -1
        return index
    def pop(self):
        current = self.head
        previous = None
        if current != None:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            if previous == None:
                self.head = None
                self.length -= 1
                return current.getData()
            else:
                previous.setNext(None)
                self.length -= 1
                return current.getData()
    def pop(self, pos):
        if pos < self.length:
            index = 0
            current = self.head
            previous = None
            if current != None:
                while index < pos:
                    previous = current
                    current = current.getNext()
                    index += 1
                if previous == None:
                    self.head = current.getNext()
                    self.length -= 1
                    return current.getData()
                else:
                    previous.setNext(current.getNext())
                    self.length -= 1
                    return current.getData()
    def insert(self, pos, item):
        if pos <= self.length:
            index = 0
            current = self.head
            previous = None
            if current == None:
                temp = Node(item)
                self.head = temp
                self.length += 1
            else:
                while index < pos:
                    previous = current
                    current = current.getNext()
                    index += 1
                if previous == None:
                    temp = Node(item)
                    temp.setNext(current)
                    self.head = temp
                    self.length += 1
                else:
                    temp = Node(item)
                    temp.setNext(current)
                    previous.setNext(temp)
                    self.length += 1
    def slice(self, start, stop):
        outputList = []
        if stop <= self.length and start <= stop:
            index = 0
            current = self.head
            while index < stop:
                if index >= start:
                    outputList.append(current.getData())
                current = current.getNext()
                index += 1
        return outputList