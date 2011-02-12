
'''
Created on Apr 9, 2009

@author: joeg
'''
from functools import reduce


def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x,y: x*y, [x for x in range(1,n+1)])

def nthPermutation(s, n):
    digits = list(s)    
    length = len(digits)
    status = []
    for i in range(length):
        status.append('AVAIL')
    pos = 0
    iterations = 0
    output = ''
    
    while length > 0:
        iterations = iterations + factorial(length-1)
#        if iterations == n:
#            return output
        if iterations >= n:
            output = output + digits[pos]
            status[pos] = 'DONE'
            iterations = iterations - factorial(length-1)
            length = length - 1
            for i in range(len(status)):
                if status[i] != 'DONE':
                    status[i] = 'AVAIL'
        else:
            status[pos] = 'CHECKED'
            
        for i in range(len(status)):
            if status[i] == 'AVAIL':
                pos = i
                break
    return output
        
print(nthPermutation('0123456789', 1000000))