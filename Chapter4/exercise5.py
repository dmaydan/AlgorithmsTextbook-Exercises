# WRITE IMPLEMENTATIONS FOR A RECURSIVE AND ITERATIVE FIBONACCI ALGORITHM
def recursive_fibonacci(number):
	if number == 1 or number == 2:
		return 1
	else:
		return recursive_fibonacci(number-1) + recursive_fibonacci(number-2)

print(recursive_fibonacci(6))
# The problem with the recursive implementation is that it will reevaluate the same fibonacci number many times
# To fix this problem, we implement an iterative solution (dynamic programming)

def iterative_fibonacci(number):
	startList = [1, 1]
	while len(startList) < number:
		startList.append(startList[-1] + startList[-2])
	return startList[number - 1]

print(iterative_fibonacci(6))