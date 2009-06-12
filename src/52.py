'''
Created on Apr 10, 2009

@author: joeg
'''

for n in range(1,1000000):
    n_2 = 2*n
    n_3 = 3*n
    n_4 = 4*n
    n_5 = 5*n
    n_6 = 6*n
    
    if sorted([x for x in str(n)]) == sorted([x for x in str(n_2)]) \
        and sorted([x for x in str(n)]) == sorted([x for x in str(n_3)]) \
        and sorted([x for x in str(n)]) == sorted([x for x in str(n_4)]) \
        and sorted([x for x in str(n)]) == sorted([x for x in str(n_5)]) \
        and sorted([x for x in str(n)]) == sorted([x for x in str(n_6)]):
        print(n)