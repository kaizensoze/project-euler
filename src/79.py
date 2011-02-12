'''
Created on Jun 13, 2009

@author: anon
'''
f = open('../keylog.txt')
passcodes = sorted(list(set([x.strip() for x in f.readlines()])))
# the rest done by hand on whiteboard
