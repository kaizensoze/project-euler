
from ProjectEulerLibrary import isPrime

# find odd non-prime that != prime + 2*square

# iterate on odd non-prime numbers starting with... 9
# 2*2 + 5

done = False

compositeOdd = (x for x in range(3,10000000000) if x%2 == 1 and not isPrime(x))

while not done:
    canBeWritten = False
    x = next(compositeOdd)
    i = 1
    amt = 2*(i**2)
    while amt <= x:
        print('x: ', x)
        print('amt: ', amt)
        if isPrime(x - amt):
            canBeWritten = True
            break
        i += 1
        amt = 2*(i**2)
    if not canBeWritten:
        print(x)
        done = True
