'''
Created on Apr 8, 2009

@author: anon
'''

sum = 0
for x in range(2,1000000):
    digits = [int(y) for y in list(str(x))]
    digitsSum = 0
    for digit in digits:
        digitsSum = digitsSum + (digit ** 5)
    if x == digitsSum:
        sum = sum + x

print(sum)
