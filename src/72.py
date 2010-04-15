
reduced = set([])

def gcd(a,b):
    while a:
        a, b = b%a, a
    return b

def reduce(n,d):
    c = gcd(n,d)
    return int(n/c), int(d/c)

d = 1000000

def output(x):
    return str(x[0]) + '/' + str(x[1])

for i in range(1,d+1):
    for j in range(1,d+1):
        if i < j:
            reduced.add(output(reduce(i,j)))

print(reduced)
print(len(reduced))
