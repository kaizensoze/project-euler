'''
Created on Apr 18, 2009

@author: anon
'''

from ProjectEulerLibrary import isPandigital

maxProduct = 0

for n in range(1,9999):
    product = ''
    i = 1
    while len(str(product)) < 9:
        newProduct = n * i
        product = product + str(newProduct)
        i = i + 1
    if isPandigital(int(product)):
        if int(product) > maxProduct:
            maxProduct = int(product)

print(maxProduct)
