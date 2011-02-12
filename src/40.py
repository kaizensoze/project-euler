'''
Created on Apr 10, 2009

@author: joeg
'''

s = ''
for n in range(1,300000):
    s = s + str(n)

prod = 1
for i in range(6):
    prod = prod * int(s[(10 ** i)-1]) 
    
print(prod)
