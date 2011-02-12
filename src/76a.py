#!/usr/python

import math

m = {}

def main():
    n = 100
    result = p(n)
    print(result)

def p(n):
    return 1 + sum([p_i(k,n-k) for k in range(1, int(math.floor(n/2)))])

def p_i(k, n):
    global m

    if k > n:
        return 0
    elif k == n:
        return 1
    else:
        if (k+1, n) not in m:
            a = p_i(k+1, n)
            m[(k+1, n)] = a
        else:
            a = m[(k+1, n)]

        if (k, n-k) not in m:
            b = p_i(k, n-k)
            m[(k, n-k)] = b
        else:
            b = m[(k, n-k)]

        return a + b

if __name__ == "__main__":
    main()
