# MODIFY THE INFIX POSTFIX ALGORITHM SO THAT IT CAN HANDLE ERRORS
from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
	error = error_check(infixexpr)
	if error:
		return error
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opStack = Stack()
	postfixList = []
	tokenList = infixexpr.split()

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and \
			   (prec[opStack.peek()] >= prec[token]):
				  postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())
	return " ".join(postfixList)

def error_check(infixexpr):
	# The infixexpr must be separated by spaces
	if not no_foreign_char(infixexpr):
		return "Foreign Characters"
	if not balanced_paren(infixexpr):
		return "Unbalanced Parentheses"
	if not operator_between_operands(infixexpr):
		return "Invalid Infix"
	else:
		return False
def operator_between_operands(infixexpr):
	tokenList = infixexpr.split()
	while "(" in tokenList:
		tokenList.remove("(")
	while ")" in tokenList:
		tokenList.remove(")")
	for i in range(len(tokenList)):
		if tokenList[i] in ["*", "/", "+", "-", "("]:
			try:
				previousToken = tokenList[i-1]
				nextToken = tokenList[i + 1]
				if not previousToken in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and not previousToken in "0123456789":
					raise Exception("Previous token not operand")
				if not nextToken in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and not nextToken in "0123456789":
					raise Exception("Next token not operand")
			except:
				# Either the it the left and right tokens were not operands or they did not exist
				return False
	return True
def is_not_foreign_char(char):
	if not char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and not char in "0123456789" and not char == "(" and not char == ")" and not char in ["*", "/", "+", "-", "("]:
		return False
	else:
		return True
def no_foreign_char(infixexpr): # check for foreign characters
	tokenList = infixexpr.split()
	for token in tokenList:
		if not is_not_foreign_char(token):
			return False
	return True
def balanced_paren(infixexpr):
	parenStack = Stack()
	tokenList = infixexpr.split()
	for token in tokenList:
		if token == "(":
			parenStack.push(token)
		elif token == ")":
			if parenStack.isEmpty():
				return False
			else:
				parenStack.pop()
	if parenStack.isEmpty():
		return True
	else:
		return False

print(infixToPostfix("A * B + (  C * ) A"))


