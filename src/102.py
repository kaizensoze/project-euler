from math import *

"""
NOTE: I keep forgetting how awful the default math module is.
      I need to switch to scipy or numpy.
"""

def det(a,b):
    return a.real*b.imag - a.imag*b.real

def dot(a,b):
    return a.real*b.real + a.imag*b.imag

def mag(a):
    return sqrt(a.real**2 + a.imag**2)

count = 0
o = complex(0,0)
f = open('../triangles.txt')
f_gen = (x for x in f)
while True:
    try:
        p = [int(x) for x in next(f_gen).strip().split(',')]
        a = complex(p[0], p[1])
        b = complex(p[2], p[3])
        c = complex(p[4], p[5])

        v1 = o-a
        v2 = o-b
        v3 = o-c

        angles1 = acos(dot(v1,v2)/(mag(v1)*mag(v2)))
        angles2 = acos(dot(v2,v3)/(mag(v2)*mag(v3)))
        angles3 = acos(dot(v3,v1)/(mag(v3)*mag(v1)))

        sumAngles = angles1 + angles2 + angles3
        sumAngles = sumAngles * (180/pi)
        print(sumAngles)
        if abs(360 - sumAngles) < .000001:
            count +=1
    except StopIteration:
        break

print(count)
