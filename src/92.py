
def mark(wh, records):
    for x in records:
        wh.add(x)

def run():
    arrivals = []
    willHit = set([])
    willNotHit = set([])
    for x in range(1,10000000):
        print(x)
        records = []
        n = x
        while 1:
            if n == 89 or n in willHit:
                mark(willHit, records)
                arrivals.append(x)
                break
            elif n in records or n in willNotHit:
                willNotHit.add(n)
                break
            else:
                records.append(n)
                n = sum([int(x)**2 for x in str(n)])
    print(arrivals)
    print(len(arrivals))
run()
