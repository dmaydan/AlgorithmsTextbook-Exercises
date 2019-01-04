# WRITE A PROGRAM THAT SOLVES THE FOLLOWING PROBLEM: THREE MISSIONARIES AND THREE CANNIBALS COME TO A RIVER AND FIND A BOAT THAT HOLDS TWO PEOPLE. EVERYONE MUST GET ACROSS THE RIVER TO CONTINUE ON THE JOURNEY. HOWEVER, IF THE CANNIBALS EVER OUTNUMBER THE MISSIONARIES ON EITHER BANK, THE MISSIONARIES WILL BE EATEN. FIND A SERIES OF CROSS THAT WILL GET EVERYONE SAFETLY TO THE OTHER SIDE OF THE RIVER
# I used essentially the same algorithm as I did for the previous problem - at each call, I will try to execute a step - if it doesn't work, I'll go to the next step.
# This obviously does not yield an optimal solution
def bank_solve(bankA, bankB, boatLocation, bankMemoDict, onlyChoice):
	if len(bankB) == 5:
		print((bankA,bankB))
		return True
	tupleBankA = tuple(bankA)
	tupleBankB = tuple(bankB)
	if onlyChoice or not (tupleBankA, tupleBankB) in bankMemoDict:
		print((bankA, bankB))
		bankMemoDict[(tupleBankA, tupleBankB)] = True
		possibleSteps = generate_steps(bankA, bankB, boatLocation)
		if boatLocation == "A":
			boatLocation = "B"
		elif boatLocation == "B":
			boatLocation = "A"
		worked = False
		onlyChoice = True
		for step in possibleSteps:
			if not (tuple(step[0]), tuple(step[1])) in bankMemoDict:
				onlyChoice = False
		for step in possibleSteps:
			if bank_solve(step[0], step[1], boatLocation, bankMemoDict, onlyChoice):
				worked = True
				break
		return worked
	else:
		return False
def generate_steps(bankA, bankB, boatLocation):
	possibleSteps = []
	if boatLocation == "A":
		cannibalCount = bankA.count(0)
		missionaryCount = bankA.count(1)
		if cannibalCount > 0:
			newBankA = bankA[:]
			newBankA.remove(0)
			newBankB = bankB[:]
			newBankB.append(0)
			possibleSteps.append((newBankA, newBankB))
		if missionaryCount > 0:
			newBankA = bankA[:]
			newBankA.remove(1)
			newBankB = bankB[:]
			newBankB.append(1)
			possibleSteps.append((newBankA, newBankB))
		if missionaryCount >= 2:
			newBankA = bankA[:]
			newBankA.remove(1)
			newBankA.remove(1)
			newBankB = bankB[:]
			newBankB.append(1)
			newBankB.append(1)
			possibleSteps.append((newBankA, newBankB))
		if cannibalCount == 2:
			newBankA = bankA[:]
			newBankA.remove(0)
			newBankA.remove(0)
			newBankB = bankB[:]
			newBankB.append(0)
			newBankB.append(0)
			possibleSteps.append((newBankA, newBankB))
		if missionaryCount > 0 and cannibalCount > 0:
			newBankA = bankA[:]
			newBankA.remove(0)
			newBankA.remove(1)
			newBankB = bankB[:]
			newBankB.append(0)
			newBankB.append(1)
			possibleSteps.append((newBankA, newBankB))
	if boatLocation == "B":
		cannibalCount = bankB.count(0)
		missionaryCount = bankB.count(1)
		if cannibalCount > 0:
			newBankA = bankA[:]
			newBankA.append(0)
			newBankB = bankB[:]
			newBankB.remove(0)
			possibleSteps.append((newBankA, newBankB))
		if missionaryCount > 0:
			newBankA = bankA[:]
			newBankA.append(1)
			newBankB = bankB[:]
			newBankB.remove(1)
			possibleSteps.append((newBankA, newBankB))
		if missionaryCount >= 2:
			newBankA = bankA[:]
			newBankA.append(1)
			newBankA.append(1)
			newBankB = bankB[:]
			newBankB.remove(1)
			newBankB.remove(1)
			possibleSteps.append((newBankA, newBankB))
		if cannibalCount == 2:
			newBankA = bankA[:]
			newBankA.append(0)
			newBankA.append(0)
			newBankB = bankB[:]
			newBankB.remove(0)
			newBankB.remove(0)
			possibleSteps.append((newBankA, newBankB))
		if missionaryCount > 0 and cannibalCount > 0:
			newBankA = bankA[:]
			newBankA.append(0)
			newBankA.append(1)
			newBankB = bankB[:]
			newBankB.remove(0)
			newBankB.remove(1)
			possibleSteps.append((newBankA, newBankB))
	possibleStepsClone = []
	for i in range(len(possibleSteps)):
		missionaryCountA = possibleSteps[i][0].count(1)
		missionaryCountB = possibleSteps[i][1].count(1)
		cannibalCountA = possibleSteps[i][0].count(0)
		cannibalCountB = possibleSteps[i][1].count(0)
		if not (cannibalCountA > missionaryCountA and missionaryCountA != 0 or cannibalCountB > missionaryCountB and missionaryCountB != 0):
			possibleSteps[i][0].sort()
			possibleSteps[i][1].sort()
			possibleStepsClone.append(possibleSteps[i])
	return possibleStepsClone

bank_solve([0, 0, 1, 1, 1], [], "A", {}, False)


