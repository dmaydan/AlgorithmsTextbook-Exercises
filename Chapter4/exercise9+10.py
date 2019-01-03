# WRITE A PROGRAM TO SOLVE THE FOLLOWING PROBLEM: YOU HAVE TWO JUGS: A 4 GALLON JUG AND A 3 GALLON JUG. NEITHER OF THE JUGS HAS MARKINGS ON IT. THERE IS A PUMP THAT CAN BE USED TO FILL THE JUGS WITH WATER. HOW CAN YOU GET EXACTLY TWO GALLONS OF WATER IN THE 4 GALLON JUG.
# GENERALIZE THE PROBLEM SO THAT THE SIZES OF EACH JUG AND THE FINAL AMOUNG OF WATER TO BE LEFT IN THE LARGER JUG ARE PARAMETERS TO THE SOLUTION.

'''
ALGORITHM DESCRIPTION:
There are 6 possible ways to modify the current state: fill jug a, fill jug b, 
pour jug a into jug b, pour jug b into jug a, empty jug a, or empty jug b. 
During each all of the jug_solve function, we want to try out each possibility.
However, we do not want to try out a modificatio that will lead us to a state
that we have already been in because we always want to reach a new state. We
accomplish this with memoization. The algorithm will always execute the first
step which does not bring us back to a previous state. Without memoization,
the algorithm would keep pursuing the first step ad infinitum. Even though 
the first step will still be called when it leads to a previous state,
it will not call jug_solve and will not print to the console so it is
as if it were not called. Without returning worked, only the second to last
call prior to the end will have True value for worked and stop recursing. 
The True value will not be provided to previous calls so they will
continue recursing. That's why we need to return worked so that previous
calls know to stop searching. We return false if we have reached a state
that we have already visited - this is technically not required because
with or without it, that step will not recurse into further steps. When
execution returns to the function that called the function which terminated
in false, that function will attempt to modify the state by calling the
next possible step.
'''
def pour(jugA, currentJugA, jugB, currentJugB):
	permanentJugA = currentJugA
	currentJugA = currentJugA - (jugB - currentJugB)
	if currentJugA < 0:
		currentJugA = 0
	currentJugB = currentJugB + permanentJugA
	if currentJugB > jugB:
		currentJugB = jugB
	return (currentJugA, currentJugB)
def jug_solve(jugA, currentJugA, jugB, currentJugB, desiredAmt, jugMemoDict):
    if currentJugA == desiredAmt:
        print((currentJugA,currentJugB))
        return True
    (pouredJugA1, pouredJugB1) = pour(jugA, currentJugA, jugB, currentJugB)
    (pouredJugB2, pouredJugA2 )= pour(jugB, currentJugB, jugA, currentJugA)
    if not (currentJugA, currentJugB) in jugMemoDict:
        print((currentJugA,currentJugB))
        jugMemoDict[(currentJugA, currentJugB)] = True
        worked = jug_solve(jugA, jugA, jugB, currentJugB, desiredAmt, jugMemoDict) or \
                jug_solve(jugA, currentJugA, jugB, jugB, desiredAmt, jugMemoDict) or \
                jug_solve(jugA, pouredJugA1, jugB, pouredJugB1, desiredAmt, jugMemoDict) or \
                jug_solve(jugA, pouredJugA2, jugB, pouredJugB2, desiredAmt, jugMemoDict) or \
                jug_solve(jugA, 0, jugB, currentJugB, desiredAmt, jugMemoDict) or \
                jug_solve(jugA, currentJugA, jugB, 0, desiredAmt, jugMemoDict)
        return worked
    else:
        return False

jug_solve(4, 0, 3, 0, 2, {})
