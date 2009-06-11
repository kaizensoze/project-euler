'''
Created on Apr 3, 2009

@author: anon
'''
from ProjectEulerLibrary import generatePythagoreanTriples

print(reduce(lambda x,y: x*y, generatePythagoreanTriples(1000)))
