# IMPLEMENT A RECURSIVE ALGORITHM TO FIND THE SUM OF ALL ELEMENTS IN A LIST WHERE THE ELEMENTS CAN BE LISTS AND THE ELEMENTS WITHIN THE LISTS CAN BE LISTS THEMSELVES AND SO FORTH

def recursive_list_of_lists_sum(alist):
	if not isinstance(alist, list):
		return alist
	sum = 0
	for element in alist:
		sum += recursive_list_of_lists_sum(element)
	return sum
print(recursive_list_of_lists_sum([[1,2],[[3,4],[5,6]]]))