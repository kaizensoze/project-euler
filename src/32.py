'''
Created on Jun 12, 2009

@author: anon
'''
1,4,4
2,3,4

a = [1,2,3,4,5,6,7,8,9]
tried_products = []
pandigitals = []
sum = 0

for x in range(1,9+1):
    for y in range(1000,9999+1):
        p = x * y
        if len(str(p)) == (9 - len(str(x)) - len(str(y))):
            b = []
            b.extend([int(k) for k in str(x)])
            b.extend([int(k) for k in str(y)])
            b.extend([int(k) for k in str(p)])
            b.sort()
            if b == a and p not in tried_products:
                sum += p
                tried_products.append(p)
                pandigitals.append(p)

for x in range(10,99+1):
    for y in range(100,999+1):
        p = x * y
        if len(str(p)) == (9 - len(str(x)) - len(str(y))):
            b = []
            b.extend([int(k) for k in str(x)])
            b.extend([int(k) for k in str(y)])
            b.extend([int(k) for k in str(p)])
            b.sort()
            if b == a and p not in tried_products:
                sum += p
                tried_products.append(p)
                pandigitals.append(p)
print(sum)
print(sorted(pandigitals))