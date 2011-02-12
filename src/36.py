'''
Created on Apr 9, 2009

@author: joeg
'''

def toBinary(n):
    binOutput = ''
    while n >= 1: 
        r = n % 2       
        n = int(n/2)
        binOutput = str(r) + binOutput 
    return binOutput 

def isPalindrome(s):
    return s == s[::-1]

sum = 0
for i in range(1000000):
    if isPalindrome(str(i)) and isPalindrome(str(toBinary(i))):
        sum = sum + i
        
print(sum)        