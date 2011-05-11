#!/usr/python

from decimal import *
from fractions import Fraction
import math

def main():
    max_iterations = 10
    solutions = []
    #n = math.e
    #n = math.sqrt(2)
    n = 3.245
    find_convergent(n, solutions, 0, max_iterations)
    print(solutions)

def find_convergent(n, solutions, iterations, max_iterations):
    if iterations == 5:
        return
    int_part = int(Decimal(str(n)))
    frac_part = float(n) - float(int_part)
    if frac_part <= 0.0 or len(solutions) == max_iterations - 1:
        print("STOP (%s)" % int_part)
        return int_part
    else:
        frac_reciprocal = 1.0/frac_part
        print("%s %s %s %s" % (n, int_part, frac_part, frac_reciprocal))
        soln = int_part + float(1)/find_convergent(frac_reciprocal, solutions, iterations+1, max_iterations)
        solutions.insert(0, (soln, Fraction("%s" % soln)))
        return soln

if __name__ == "__main__":
    main()

