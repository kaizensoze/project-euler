import gmpy
import itertools

LIMIT = 1000

def concat(x, y):
    return int(str(x)+str(y))

def concatenable(x, y):
    check_one = concat(x, y)
    check_two = concat(y, x)
    return gmpy.is_prime(check_one) and gmpy.is_prime(check_two)

def main():
    global LIMIT
    m = {}
    primes = [x for x in range(3, LIMIT) if gmpy.is_prime(x)]
    for x in primes:
        for y in primes:
            if x == y:
                continue

            if concatenable(x, y):
                if x not in m:
                    m[x] = set([x])
                m[x].add(y)

                if y not in m:
                    m[y] = set([y])
                m[y].add(x)

    for x in m.iterkeys():
        count = 0
        solution = set([x])
        for y in m[x]:
            if x != y and len(m[x] & m[y]) >= 5:
                solution.add(y)
                count += 1
                if count == 5:
                    print(solution)
                    return
    '''
    print(sorted([x for x in m[3]]))
    print(sorted([x for x in m[7]]))
    print(sorted([x for x in m[109]]))
    print(sorted([x for x in m[673]]))
    a = m[3]
    b = m[7]
    c = m[109]
    d = m[673]
    print(sorted(a & b & c & d))
    '''

if __name__ == "__main__":
    main()

