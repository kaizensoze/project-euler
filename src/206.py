from math import sqrt

def run():

    n = '1_2_3_4_5_6_7_8_900'

    for a in range(10):
        n = n[0] + str(a) + n[2:]
        for b in range(10):
            n = n[0:3] + str(b) + n[4:]
            for c in range(10):
                n = n[0:5] + str(c) + n[6:]
                for d in range(10):
                    n = n[0:7] + str(d) + n[8:]
                    for e in range(10):
                        n = n[0:9] + str(e) + n[10:]
                        for f in range(10):
                            n = n[0:11] + str(f) + n[12:]
                            for g in range(10):
                                n = n[0:13] + str(g) + n[14:]
                                for h in range(10):
                                    n = n[0:15] + str(h) + n[16:]
                                    print(n)
                                    root = sqrt(float(n))
                                    if root - int(root) == 0:
                                        print(root)
                                        return
run()
