'''
Created on Apr 10, 2009

@author: joeg
'''

def generateTriangleNumbers(howManyToGenerate):
    triangleNumbers = []
    for n in range(1,howManyToGenerate):
        triangle = int(0.5 * n * (n + 1))
        triangleNumbers.append(triangle)
    return triangleNumbers

def generatePentagonalNumbers(howManyToGenerate):
    pentagonalNumbers = []
    for n in range(1,howManyToGenerate):
        pentagon = int(0.5 * n * (3*n - 1))
        pentagonalNumbers.append(pentagon)
    return pentagonalNumbers    

def generateHexagonalNumbers(howManyToGenerate):
    hexagonalNumbers = []
    for n in range(1,howManyToGenerate):
        hexagon = int(n * (2*n - 1))
        hexagonalNumbers.append(hexagon)
    return hexagonalNumbers    
    
    
n = 100000  # probably safe to set this a lot lower for future reference
triangleNumbers = generateTriangleNumbers(n)
pentagonalNumbers = generatePentagonalNumbers(n)
hexagonalNumbers = generateHexagonalNumbers(n)

for x in triangleNumbers:
    if x in pentagonalNumbers and x in hexagonalNumbers:
        print(x)
