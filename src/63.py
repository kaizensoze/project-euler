'''
Created on Apr 14, 2009

@author: anon
'''

count = 0

for i in range(1,100):
    print("Working on", i, "digit numbers")
    min = 10 ** (i-1)
    max = 10 ** i
    for k in range(1,10):
        x = k ** i
        if x >= min and x < max:
            print("Found", x)
            count += 1
            
print(count)