'''
Created on Apr 20, 2009

@author: anon
'''

def left(n):
    return str(x)[:2]

def right(n):
    return str(x)[-2:]

def generate(f, limit):
    return [f(x) for x in range(limit) if 999 < f(x) < 10000]

triangle = lambda x: int( (x*(x+1)) / 2 )
triangles = generate(triangle, 10000)

square = lambda x: int(x ** 2)
squares = generate(square, 10000)

pentagon = lambda x: int( (x*(3*x-1)) / 2 )
pentagons = generate(pentagon, 10000)

hexagon = lambda x: int( x*(2*x-1))
hexagons = generate(hexagon, 10000)

heptagon = lambda x: int( (x*(5*x-3)) / 2 )
heptagons = generate(heptagon, 10000)

octagon = lambda x: int( x*(3*x-2) )
octagons = generate(octagon, 10000)

# organize each number type by their connectors
triangleLeftConnectors = {}
for x in triangles:
    left = str(x)[:2]
    if not left in triangleLeftConnectors:
        triangleLeftConnectors[left] = []
    else:
        triangleLeftConnectors[left].append(x)

#triangleRightConnectors = {}
#for x in triangles:
#    right = str(x)[-2:]
#    if not right in triangleRightConnectors:
#        triangleRightConnectors[right] = []
#    else:
#        triangleRightConnectors[right].append(x)

squareLeftConnectors = {}
for x in squares:
    left = str(x)[:2]
    if not left in squareLeftConnectors:
        squareLeftConnectors[left] = []
    else:
        squareLeftConnectors[left].append(x)

#squareRightConnectors = {}
#for x in squares:
#    right = str(x)[-2:]
#    if not right in squareRightConnectors:
#        squareRightConnectors[right] = []
#    else:
#        squareRightConnectors[right].append(x)

pentagonLeftConnectors = {}
for x in pentagons:
    left = str(x)[:2]
    if not left in pentagonLeftConnectors:
        pentagonLeftConnectors[left] = []
    else:
        pentagonLeftConnectors[left].append(x)

#pentagonRightConnectors = {}
#for x in pentagons:
#    right = str(x)[-2:]
#    if not right in pentagonRightConnectors:
#        pentagonRightConnectors[right] = []
#    else:
#        pentagonRightConnectors[right].append(x)

hexagonLeftConnectors = {}
for x in hexagons:
    left = str(x)[:2]
    if not left in hexagonLeftConnectors:
        hexagonLeftConnectors[left] = []
    else:
        hexagonLeftConnectors[left].append(x)

#hexagonRightConnectors = {}
#for x in hexagons:
#    right = str(x)[-2:]
#    if not right in hexagonRightConnectors:
#        hexagonRightConnectors[right] = []
#    else:
#        hexagonRightConnectors[right].append(x)

heptagonLeftConnectors = {}
for x in heptagons:
    left = str(x)[:2]
    if not left in heptagonLeftConnectors:
        heptagonLeftConnectors[left] = []
    else:
        heptagonLeftConnectors[left].append(x)

#heptagonRightConnectors = {}
#for x in heptagons:
#    right = str(x)[-2:]
#    if not right in heptagonRightConnectors:
#        heptagonRightConnectors[right] = []
#    else:
#        heptagonRightConnectors[right].append(x)

octagonLeftConnectors = {}
for x in octagons:
    left = str(x)[:2]
    if not left in octagonLeftConnectors:
        octagonLeftConnectors[left] = []
    else:
        octagonLeftConnectors[left].append(x)

#octagonRightConnectors = {}
#for x in octagons:
#    right = str(x)[-2:]
#    if not right in octagonRightConnectors:
#        octagonRightConnectors[right] = []
#    else:
#        octagonRightConnectors[right].append(x)

# each position in taken array represents a number type
taken = [False] * 6
numbers = []

leftConnectors = [triangleLeftConnectors, squareLeftConnectors,  \
                  pentagonLeftConnectors, hexagonLeftConnectors, \
                  heptagonLeftConnectors, octagonLeftConnectors]

#rightConnectors = [triangleRightConnectors, squareRightConnectors, \
#                  pentagonRightConnectors, hexagonRightConnectors, \
#                  heptagonRightConnectors, octagonRightConnectors]

#print(triangles)
#print(triangleLeftConnectors)
#print(triangleRightConnectors)

done = False
while not done:
    if len(numbers) == 6:
        if left(numbers[0]) == right(numbers[-1]):
            done = True
        else:
            numbers.pop()
    
    if len(numbers) == 0:
        # try any number
        blah = 'blah' # TODO: what is this all about?
    else:
        # find a number whose type is not taken and whose left == right of previous
        #TODO: need to mark position in each list
        nextNumbers = [x[right(previous)] for i,x in enumerate(leftConnectors) if not taken[i]]
        


print(numbers)
