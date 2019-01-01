# GIVEN A LIST OF NUMBERS IN RANDOM ORDER, WRITE AN ALGORITHM THAT WORKS IN O(nlog(n)) TO FIND THE KTH SMALLEST NUMBER IN THE LIST
inputList = [10, 6, 31, 78, 34, 18, 104, 23]
def find_kth_smallest(list, k):
	list.sort()
	if ((k) > len(list)):
		return False
	else:
		return list[k-1]
print(find_kth_smallest(inputList, 9))