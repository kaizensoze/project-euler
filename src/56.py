'''
Created on Apr 13, 2009

@author: anon
'''

maxDigitSum = 0
for a in range(2,100):
    for b in range(2,100):
        result = a**b
        digitSum = sum([int(x) for x in str(result)])
        if digitSum > maxDigitSum:
             maxDigitSum = digitSum
print(digitSum)