
chains = 0

def factorial(n):
    if n == 0:
        return 1
    return reduce(lambda x,y: x*y, range(1,n+1))

def factorialSum(n):
    return reduce(lambda x,y: x+y, [factorial(int(i)) for i in str(n)])

def runChain(n):
    global chains
    term_count = 0
    terms_encountered = []
    n_orig = n

    while n not in terms_encountered:
        term_count += 1
        n_old = n
        n = factorialSum(n)
        terms_encountered.append(n_old)
        #print(n_old)

    if term_count == 60:
        chains += 1
    #print(term_count)

#'''
for i in range(1, 1000000):
    print(i)
    runChain(i)
print(chains)
#'''
