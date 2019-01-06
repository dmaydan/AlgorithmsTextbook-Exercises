# DRAW PASCAL'S TRIANGLE
def pascal(numRows):
	index = 0
	pascalTriangle = []
	while index < numRows:
		if index == 0:
			pascalTriangle.append([1])
		else:
			temp = []
			for i in range(index + 1):
				if i == 0:
					temp.append(1)
				elif i == index:
					temp.append(1)
				else:
					temp.append(pascalTriangle[index-1][i- 1]+pascalTriangle[index-1][i])
			pascalTriangle.append(temp)
		index += 1
	maxLength = 0
	rowList = []
	for row in pascalTriangle:
		rowString = '  '.join(str(x) for x in row)
		if len(rowString) > maxLength:
			maxLength = len(rowString)
		rowList.append(rowString)
	for rowString in rowList:
		print(rowString.center(maxLength))
pascal(10)
