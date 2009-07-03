import math
from ProjectEulerLibrary import isPalindrome

# IT ONLY TOOK THE DURATION OF TWO FEATURE FILMS TO FINISH!!!

def SLOWisSumOfConsecSquares(x):
    stoppingPoint = (int)(math.sqrt(x))
    for i in range(1, stoppingPoint):
        value = 0
        j = i
        while value < x:
            value += (j ** 2)
            j += 1
        if value == x:
            return True
    return False

def isSumOfConsecSquares(x):
    stoppingPoint = (int)(math.sqrt(x))
    for i in range(stoppingPoint, 0, -1):
        value = x
        consecCount = 0
        j = i
        while value >= 1 and j > 0:
            value -= (j ** 2)
            j -= 1
            consecCount += 1
        if value == 0 and consecCount > 1:
            return True
    return False

isSumOfConsecSquares(595)

solutions = []
palindromes = [x for x in range(1,10**8) if isPalindrome(x)]
#solutions = [x for x in palindromes if isSumOfConsecSquares(x)]
for x in palindromes:
    if isSumOfConsecSquares(x):
        solutions.append(x)
        print(x)
print(solutions)
print(sum(solutions))
