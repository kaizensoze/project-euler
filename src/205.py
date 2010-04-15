import decimal

pCount = 0
pt = {}

cCount = 0
ct = {}

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                for e in range(1,5):
                    for f in range(1,5):
                        for g in range(1,5):
                            for h in range(1,5):
                                for i in range(1,5):
                                    sum = a+b+c+d+e+f+g+h+i
                                    if sum in pt.keys():
                                        pt[sum] += 1
                                    else:
                                        pt[sum] = 1
                                    pCount += 1

for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        sum = a+b+c+d+e+f
                        if sum in ct.keys():
                            ct[sum] += 1
                        else:
                            ct[sum] = 1
                        cCount += 1

prob = 0
decimal.getcontext().prec = 15
c = decimal.Decimal(cCount)
p = decimal.Decimal(pCount)

for pk in pt.keys():
    for ck in ct.keys():
        if pk > ck:
            pResult = decimal.Decimal(pt[pk])
            cResult = decimal.Decimal(ct[ck])
            lProb = (pResult*cResult) / (c*p)
            prob += lProb

print(prob)
