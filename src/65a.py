#!/usr/python

from decimal import *
from fractions import Fraction
from fractions import gcd
import math

def main():
    max_iterations = 100
    int_parts = []
    n = math.e
    #n = math.sqrt(2)
    #n = 3.245
    n_curr = n
    while len(int_parts) < max_iterations:
        int_part = int(Decimal(str(n_curr)))
        int_parts.append(int_part)
        frac_part = float(n_curr) - float(int_part)
        if frac_part <= 0.0:
            break
        frac_reciprocal = 1.0/frac_part
        n_curr = frac_reciprocal
        #print("%s %s %s" % (int_part, frac_part, frac_reciprocal))
    #print(int_parts)

    solns = []
    curr = int_parts[max_iterations-1]
    for j in range(max_iterations-1,0,-1):
        curr = int_parts[j-1] + 1.0/curr
    f = (curr, Fraction("%s" % curr))
    print(f)

if __name__ == "__main__":
    main()

