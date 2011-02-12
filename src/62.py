'''
Created on Apr 21, 2009

@author: anon
'''

def generateCubes(limit):
    return [(i ** 3) for i in range(1,limit)]

def permute(s):
    if len(s) == 1:
        yield s
    else:
        for x in permute(s[1:]):
            for i in range(len(x)+1):
                yield x[:i] + s[0] + x[i:]

#print(set([int(x) for x in permute(str('343'))]))

cubeCount = 0
i = 4
done = False
limit = 10000

cubes = generateCubes(limit)

for i in range(1,limit):
    n = int(i ** 3)
    permCubes = set([int(x) for x in permute(str(n))]).intersection(set(cubes))    
    print(n, [x for x in permCubes])
    if len(permCubes) == 5:
        print(n)
        break
