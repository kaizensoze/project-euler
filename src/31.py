'''
Created on Apr 14, 2009

@author: joeg
'''

target = 200
coins = [1,2,5,10,20,50,100,200]

def p1(n):
    return 1

def p2(n):
    if n >= 0:
        return p2(n-2) + p1(n)
    else:
        return 0

def p5(n):
    if n >= 0:
        return p5(n-5) + p2(n)
    else:
        return 0

def p10(n):
    if n >= 0:
        return p10(n-10) + p5(n)
    else:
        return 0

def p20(n):
    if n >= 0:
        return p20(n-20) + p10(n)
    else:
        return 0

def p50(n):
    if n >= 0:
        return p50(n-50) + p20(n)
    else:
        return 0

def p100(n):
    if n >= 0:
        return p100(n-100) + p50(n)
    else:
        return 0

def p200(n):
    if n >= 0:
        return p200(n-200) + p100(n)
    else:
        return 0

print(p200(target))
