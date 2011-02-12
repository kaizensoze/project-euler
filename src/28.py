'''
Created on Apr 8, 2009

@author: anon
'''

diagonalSum = 1
n = 1

skipAmount = 1

while skipAmount <= 999:
    for i in range(4):
        n = n + (skipAmount + 1)
        diagonalSum = diagonalSum + n
    skipAmount = skipAmount + 2

print(diagonalSum)
