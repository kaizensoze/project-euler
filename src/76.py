#!/usr/python

import cProfile

m = {}

def main():
    n = 100
    count = get_count(n)
    #print(m)
    print(count)

def get_count(n):
    global m

    m[1] = set(tuple([1]))

    for k in range(2, n+1):
        print(k)
        results = set([])
        left = k-1
        right = k - left
        while left >= right:
            #print(left, right)
            results = results.union( reduce(left, right) )
            left -= 1
            right = k - left
        m[k] = results
    return len(m[n])

def reduce(left, right):
    global m

    #print('****', left, '****')
    results = set([])
    results.add(tuple([left, right]))
    for x in m[left]:
        #print(x)
        if type(x) is not tuple:
            x = (x,)
        if type(right) is not tuple:
            right = (right,)
        bleh = tuple(sorted(x + right))
        if bleh not in results:
            results.add(bleh)
    return results

if __name__ == "__main__":
    cProfile.run('main()', '76prof')
