'''
Created on Apr 5, 2009

@author: anon
'''

scoresTotal = 0

names = [x.strip('"') for x in open('../names.txt').read().split(',')]
names.sort()

for i in xrange(len(names)):
    scoresTotal = scoresTotal + ((i+1) * sum([(ord(x)-64) for x in names[i]]))
print(scoresTotal)
