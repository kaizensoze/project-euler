import gmpy
import itertools

LIMIT = 10

def concat(a, b):
    return int(str(a)+str(b))

def getNext(primes, n=None):
    global LIMIT

    if n is not None:
        primes = (x for x in range(n,LIMIT) if gmpy.is_prime(x) and x > n)
    try:
        res = primes.next()
    except StopIteration:
        res = -1
    return (primes, res)

def check(nums, o):
    for p in nums:
        if not gmpy.is_prime(concat(o,p)) \
           or not gmpy.is_prime(int(str(p)+str(o))):
            return False
    return True

def main():
    global LIMIT
    primes = (x for x in range(3,LIMIT) if gmpy.is_prime(x))
    nums = []

    while len(nums) < 5:
        primes, n = getNext(primes)
        print(n)
        here = 'dragons'
        if n == -1:
            primes, n = getNext(primes, nums.pop())
        if check(nums, n):
            nums.append(n)
        print(nums)
    #print(nums)

if __name__ == "__main__":
    main()

'''
(3, 7, 109, 673)
need to remove from nums if LIMIT is reached
does it need to really backtrack?
'''
