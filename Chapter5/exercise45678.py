# IMPLEMENT THE LEN METHOD FOR THE HASH TABLE MAP ADT IMPLEMENTATION
# IMPLEMENT THE IN METHOD FOR THE HASH TABLE MAP ADT IMPLEMENTATION
# IMPLEMENT A DELETION MECHANISM - HANDLE SPECIAL CIRCUMSTANCES
# IMPLEMENT QUADRATIC PROBING AS A REHASH TECHNIQUE
# IMPLEMENT A MECHANISM FOR RESIZING THE HASH TABLE WHEN THE LOAD FACTOR BECOMES TOO HIGH
class HashTable:
	def __init__(self):
		self.size = 3
		self.slots = [None] * self.size
		self.data = [None] * self.size
		self.skip = 1
	def put(self,key,data):
		self.skip = 1
		newEntryNum = self.__len__() + 1
		currentCapacity = self.size
		newLoadFactor = newEntryNum / currentCapacity
		if newLoadFactor > .75:
			self.resize()
		hashvalue = self.hashfunction(key,len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data  #replace
			else:
				nextslot = self.rehash(hashvalue,len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot,len(self.slots))

				if self.slots[nextslot] == None:
					self.slots[nextslot]=key
					self.data[nextslot]=data
				else:
					self.data[nextslot] = data #replace
	def resize(self):
		# Find 
		newSize = self.size * 2
		prime = False
		while not prime:
			prime = True
			for i in range(2, newSize):
				if newSize % i == 0:
					newSize += 1
					prime = False
					break
		self.size = newSize
		slots = self.slots
		data = self.data
		self.slots = [None] * self.size
		self.data = [None] * self.size
		print(slots)
		print(data)
		for i in range(len(slots)):
			key = slots[i]
			if key != None:
				dataItem = data[i]
				self.put(key, dataItem)
	def hashfunction(self,key,size):
		return key%size
	def rehash(self,oldhash,size):
		return (oldhash+1)%size
	def quadratic_probing(self, oldhash, size):
		newHash = (oldhash + self.skip)%size
		self.skip += 2
		return newHash
		# The increment is not constant, but the different between the increments is constant
	def get(self,key):
		self.skip = 1
		startslot = self.hashfunction(key,len(self.slots))
		data = None
		stop = False
		found = False
		position = startslot
		while not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position=self.rehash(position,len(self.slots))
				if position == startslot:
					stop = True
		return data

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)
	def __len__(self):
		length = 0
		for slot in self.slots:
			if slot != None:
				length += 1
		return length
	def __contains__(self, key):
		self.skip = 1
		startslot = self.hashfunction(key,len(self.slots))
		position = startslot
		while True:
			if self.slots[position] == key:
				return True
			else:
				position=self.rehash(position,len(self.slots))
				if position == startslot:
					return False
	def __delitem__(self, key):
		self.skip = 1
		startslot = self.hashfunction(key,len(self.slots))
		position = startslot
		while True:
			if self.slots[position] == key:
				self.slots[position] = None
				return True
			else:
				position = self.rehash(position,len(self.slots))
				if position == startslot:
					return False
h = HashTable()
h[0] = "a"
h[1] = "b"
h[2] = "c"
print(h.slots)
print(h.data)