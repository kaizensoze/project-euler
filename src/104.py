'''
Created on Jul 3, 2009

@author: anon
'''
from ProjectEulerLibrary import is1to9Pandigital

count = 2
prev = curr = 1; print(1, 1); print(2, 1)
first9 = str(curr)[:9]
last9 = str(curr)[-9:]
while not (is1to9Pandigital(first9) and is1to9Pandigital(last9)):
    temp = curr
    curr = curr + prev
    first9 = str(curr)[:9]
    last9 = str(curr)[-9:]
    prev = temp
    count = count + 1
#    print(count, curr, is1to9Pandigital(first9), is1to9Pandigital(last9))
print(count)