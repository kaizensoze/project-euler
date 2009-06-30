from ProjectEulerLibrary import isPandigital
#
# WARNING:
# 
# THIS CODE IS MORE EXTRAVAGANT THAN TONY DANZA AND THE TAP DANCE EXTRAVAGANZA
#
# VIEWER DISCRETION IS ADVISED
#

def pad(x):
    z = str(x)
    while len(z) < 3:
        z = '0' + z
    return z

g = [x for x in range(12, 987+1) if x % 17 == 0]
f = [x for x in range(12, 987+1) if x % 13 == 0 and pad(x)[1:2+1] in [pad(y)[0:1+1] for y in g]]
e = [x for x in range(12, 987+1) if x % 11 == 0 and pad(x)[1:2+1] in [pad(y)[0:1+1] for y in f]]
d = [x for x in range(12, 987+1) if x % 7 == 0 and pad(x)[1:2+1] in [pad(y)[0:1+1] for y in e]]
c = [x for x in range(12, 987+1) if x % 5 == 0 and pad(x)[1:2+1] in [pad(y)[0:1+1] for y in d]]
b = [x for x in range(12, 987+1) if x % 3 == 0 and pad(x)[1:2+1] in [pad(y)[0:1+1] for y in c]]
a = [x for x in range(12, 987+1) if x % 2 == 0 and pad(x)[1:2+1] in [pad(y)[0:1+1] for y in b]]


values = []

for t in g:
    for u in [x for x in f if pad(x)[1:2+1] == pad(t)[0:1+1]]:
        for v in [x for x in e if pad(x)[1:2+1] == pad(u)[0:1+1]]:
            for w in [x for x in d if pad(x)[1:2+1] == pad(v)[0:1+1]]:
                for x in [x for x in c if pad(x)[1:2+1] == pad(w)[0:1+1]]:
                    for y in [p for p in b if pad(p)[1:2+1] == pad(x)[0:1+1]]:
                        for z in [x for x in a if pad(x)[1:2+1] == pad(y)[0:1+1]]:
                            for zz in range(1, 9+1):
                                blah = str(zz) + pad(z) + pad(w) + pad(t)
                                print(blah)
                                if isPandigital(blah):
                                    values.append(int(blah))

print(values)
print(sum(values))
