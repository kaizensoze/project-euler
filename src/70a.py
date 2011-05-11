#!/usr/bin/python

import gmpy

n_min = None
div_min = float("inf")

p = [x for x in range(8000000, 10000000) if gmpy.is_prime(x)]
for p1 in p:
    for p2 in p:
        if p1 == p2:
            continue
        n = p1*p2
        phi = (p1-1)*(p2-1)
        div = (1.0*n)/phi
        print(n, phi, div)
        if div < div_min:
            div_min = div
            n_min = n
print(n_min)
