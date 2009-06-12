'''
Created on Apr 10, 2009

@author: joeg
'''

triangleNumbers = []
for n in range(1,1000):
    triangle = int(0.5 * n * (n + 1))
    triangleNumbers.append(triangle)

triangleWords = 0

f = open('words.txt', 'r')
words = [x.strip('"') for x in list(f.readline().split(','))]
for word in words:
    sum = 0
    for letter in word:
        sum = sum + (ord(letter)-64)
    if sum in triangleNumbers:
        triangleWords = triangleWords + 1
        
print(triangleWords)