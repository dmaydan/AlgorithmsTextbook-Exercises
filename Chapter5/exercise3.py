# IMPLEMENT THE RECURSIVE BINARY SEARCH WITHOUT THE SLICE OPERATOR BECAUSE THE SLICE OPERATOR WORKS IN O(K)
def binarySearch(alist, first, last, item):
	if first > last:
		return False
	else:
		midpoint = (first + last)//2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return binarySearch(alist, first, midpoint-1, item)
			else:
				return binarySearch(alist, midpoint+1, last, item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 0, len(testlist)-1, 3))
print(binarySearch(testlist, 0, len(testlist)-1, 13))