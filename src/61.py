#!/usr/bin/python

import random

triangle = lambda n: (n*(n+1))/2
square = lambda n: n**2
pentagon = lambda n: (n*(3*n-1))/2 
hexagon = lambda n: n*(2*n-1)
heptagon = lambda n: (n*(5*n-3))/2
octagon = lambda n: n*(3*n-2)

def generate(f):
    min_limit = 1000
    max_limit = 9999
    return [f(x) for x in range(max_limit) if min_limit <= f(x) <= max_limit]

triangles = generate(triangle)
squares = generate(square)
pentagons = generate(pentagon)
hexagons = generate(hexagon)
heptagons = generate(heptagon)
octagons = generate(octagon)

def left(n):
    return str(n)[0:2]

def right(n):
    return str(n)[2:]

def linked(x, y):
    return right(x) == left(y)

shapes = [triangles, squares, pentagons, hexagons, heptagons, octagons]
shapes.reverse()
links = {}

soln = []
shapes_available = [True] * 6

def classify():
    d = {}
    for i,shape in enumerate(shapes):
        for n in shape:
            if int(right(n)) < 10: continue
            d[n] = []
            for j,other_shape in enumerate(shapes):
                if i == j:
                    continue
                for n_other in other_shape:
                    if int(right(n_other)) < 10: continue
                    if linked(n, n_other):
                        d[n].append(n_other)
    return d

c = classify()

def pluck():
    global soln
    if len(soln) > 0:
        pluck()

for o in octagons:
    if o in c:
        soln.append(o)
        for hep in heptagons:
            if hep in c[o]:
                soln.append(hep)
                for hex in hexagons:
                    if hex in c[hep]:
                        soln.append(hex)
                        for pen in pentagons:
                            if pen in c[hex]:
                                soln.append(pen)
                                for sq in squares:
                                    if sq in c[pen]:
                                        soln.append(sq)
                                        for t in triangles:
                                            if t in c[sq]:
                                                soln.append(t)
                                            pluck()
                                    pluck()
                            pluck()
                    pluck()
            pluck()
    pluck()
print(soln)
"""
last_inserted = None

def slot_can_be_filled():
    for n in soln:
        for i,avail in [i,x for i,x in enumerate(shapes_available) if avail is True]:
            for x in c[n][i]:
                if len(c[n][i].keys()) > 0 and blah not in soln:
                    pass

def find_n_to_insert():
    global soln
    global shapes_available
    global last_inserted

    #mark shape as taken
    #set last_inserted var
    if no spot:
        return None
    else:
        return (n, i)

start_shape = random.choice(range(len(shapes)))
start_n = random.choice(shapes[start_shape])

to_insert = tuple(start_shape, start_n)
soln.append(tuple(start_shape, start_n))
shapes_available[start_shape] = False
last_inserted = to_insert

while True in shapes_available:
    n = find_n_to_insert()
    if n is None:
        soln.remove(last_inserted)
        shapes_available[last_inserted[0]] = True
    else:
        soln.insert(i, n)
"""
