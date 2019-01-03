# WRITE A PROGRAM THAT CAN CHECK AN HTML DOCUMENT FOR PROPER OPENING AND CLOSING TAGS
from pythonds.basic.stack import Stack
def are_tags_balanced(html):
	tagStack = Stack()
	for i in range(len(html)):
		character = html[i]
		if character == "<":
			already = False
			if not tagStack.isEmpty():
				if tagStack.peek() == "OPEN":
					nextCharacter = html[i+1]
					if nextCharacter == "/":
						tagStack.pop()
						tagStack.push(character+nextCharacter)
						already = True
			if not already:
				tagStack.push(character)
		elif character == ">":
			if tagStack.isEmpty():
				return False
			if tagStack.peek() == "<":
				tagStack.pop()
				tagStack.push("OPEN")
			elif tagStack.peek() == "</":
				tagStack.pop()
			else:
				return False
		print(tagStack.items)
	if not tagStack.isEmpty():
		return False

	else:
		return True
myHtml = """
			<html>
				<head>
					<title></title>
				</head>
				<body>
				</body>
			</html>
		"""
print(are_tags_balanced(myHtml))