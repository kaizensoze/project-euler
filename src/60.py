import gmpy

LIMIT = 10000
n = 5

def concat(x, y):
    return int(str(x)+str(y))

def concatenable(x, y):
    check_one = concat(x, y)
    check_two = concat(y, x)
    return gmpy.is_prime(check_one) and gmpy.is_prime(check_two)

def main():
    global LIMIT, n
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

    for x in sorted(m.iterkeys()):
        count = 0
        solution = set([x])
        for y in sorted(m[x]):
            if x != y and len(m[x] & m[y]) > n:
                print(x, y)
                print(sorted(m[x]))
                print(sorted(m[y]))
                print('\n')
                solution.add(y)
                count += 1
                if count == n:
                    print(solution)
                    return

if __name__ == "__main__":
    main()

