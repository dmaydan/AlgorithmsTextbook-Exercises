# CREATE A BINARY HEAP WITH A LIMITED HEAP SIZE SO THAT IT ONLY KEEPS TRACK OF THE N MOST IMPORTANT ITEMS. IF THE HEAP GROWS IN SIZE TO MORE THAN N ITEMS THE LEAST IMPORTANT ITEM IS DROPPED.
class BinHeap:
    def __init__(self, limit):
        self.heapList = [0]
        self.currentSize = 0
        self.limit = limit
    def dropExtra(self):
      lowestPriority = None
      lowestPriorityIndex = None
      for i in range(1, len(self.heapList)):
        if not lowestPriority or self.heapList[i] > lowestPriority:
          lowestPriority = self.heapList[i]
          lowestPriorityIndex = i
      self.currentSize -= 1
      self.heapList[lowestPriorityIndex] = self.heapList[-1]
      self.heapList.pop()
      self.percDown(lowestPriorityIndex)
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
      if self.currentSize > self.limit:
      	self.dropExtra()


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
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval
  
    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
              
bh = BinHeap(5)
bh.insert(1)
bh.insert(2)
bh.insert(3)
bh.insert(2)
bh.insert(5)
print(bh.heapList)

