# SUPPOSE YOU ARE A COMPUTER SCIENTIST/ART THIEF WHO HAS BROKEN INTO A MAJOR ART GALLERY. ALL YOU WITH YOU TO HAUL OUT YOUR STOLEN ART IS YOUR KNAPSACK WHICH ONLY HOLDS W POUNDS OF ART, BUT FOR EVERY PIECE OF ART YOU KNOW ITS VALUE AND ITS WEIGHT. WRITE A DYNAMIC PROGRAMMING FUNCTION TO HELP YOU MAXIMIZE PROFIT.
def dp_knapsack_solver(W, weightToValue):
	maxProfitByWeight = {}
	valuesUsed = {}
	for weight in range(W+1):
		maxProfit =  maxProfitByWeight[weight - 1] if weight > 0 else 0
		itemUsed = 0
		maxPriorWeight = 0
		maxPriorWeightIndex = 0
		for item in [item for item in weightToValue if item <= weight]:
			tempMaxPriorWeight = 0
			tempMaxPriorWeightIndex = 0
			for i in range(weight-item, 0, -1):
				if maxProfitByWeight[i] > tempMaxPriorWeight and not item in valuesUsed[i]:
					tempMaxPriorWeight = maxProfitByWeight[i]
					tempMaxPriorWeightIndex = i
			if maxProfitByWeight[tempMaxPriorWeightIndex] + weightToValue[item] > maxProfit:
				maxProfit = maxProfitByWeight[tempMaxPriorWeightIndex] + weightToValue[item]
				itemUsed = item
				maxPriorWeight = tempMaxPriorWeight
				maxPriorWeightIndex = tempMaxPriorWeightIndex
		maxProfitByWeight[weight] = maxProfit
		if weight == 0:
			valuesUsed[weight] = [0]
		else:
			if itemUsed != 0:
				valuesUsed[weight] = valuesUsed[maxPriorWeightIndex][:]
				valuesUsed[weight].append(itemUsed)
			else:
				valuesUsed[weight] = valuesUsed[weight - 1][:]
		if weight == 10:
			print(valuesUsed[weight])
	return maxProfitByWeight
print(dp_knapsack_solver(20, {2:3, 3:4,4:8,5:8,9:10}))
# THE WEIGHTS MUST BE UNIQUE BECAUSE I AM USING THEM TO IDENTIFY ITEMS AND DETERMINE UNIQUENESS (AVOID DUPLICATES)
# THIS CAN BE EASILY FIXED BY CREATING AN ITEM CLASS AND IDENTIFYING ITEMS IN SUCH A WAY