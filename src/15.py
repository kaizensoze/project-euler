'''
Created on Apr 4, 2009

@author: anon
'''

totalRoutes = []

def doPermute(inp, out, used, length, level):
    if level == length:
#        totalRoutes.append(out)
        print(out)
        return
    
    for i in xrange(length):
        if used[i]:
            continue
        
        out = out + inp[i]
        used[i] = True
        doPermute(inp, out, used, length, level+1)
        used[i]= False
        out = out[0:(len(out)-1)]

def permute(str):
    length = len(str)
    used = []
    for x in range(length):
        used.append(False)
    out = ''
    inp = [x for x in str]
    doPermute(inp, out, used, length, 0)


n = 2
possibleRoutes = '123'
#for x in range(n):
#    possibleRoutes = possibleRoutes + 'D'
#    possibleRoutes = possibleRoutes + 'R'
permute(possibleRoutes)    
print(len(totalRoutes))
