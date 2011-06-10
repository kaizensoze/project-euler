import gmpy

LIMIT = 10000
n = 5

def concat(x, y):
    return int(str(x)+str(y))

def concat_is_prime(x, y):
    check_one = concat(x, y)
    check_two = concat(y, x)
    return gmpy.is_prime(check_one) and gmpy.is_prime(check_two)

def main():
    global LIMIT, n
    s = []
    primes = [x for x in range(3, LIMIT) if gmpy.is_prime(x)]
    for x in primes:
        del s[:]
        s.append(x)
        for y in primes:
            if x == y:
                continue
            
            all_good = True
            for a in s:
                if not concat_is_prime(a, y):
                    all_good = False
                    break
            if all_good:
                s.append(y)

            if len(s) == n:
                print(s, sum(s))
                return

if __name__ == "__main__":
    main()

