# WRITE A RECURSIVE FUNCTION TO REVERSE A LIST
def reverse(listToReverse):
	if len(listToReverse) == 1:
		return listToReverse
	else:
		return reverse(listToReverse[1:]) + listToReverse[0:1]
print(reverse([1]))