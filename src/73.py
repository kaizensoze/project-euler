#!/usr/python

def main():
    limit = 12000
    fractions = []
    existing_vals = set([])
    for d in range(2,limit+1):
        for n in range(1,d):
            frac = float(n)/d
            if frac not in existing_vals and frac > float(1)/3 and frac < float(1)/2:
                fractions.append(frac)
            existing_vals.add(frac)
        print(d)
    #fractions.sort()
    print(len(fractions))

if __name__ == "__main__":
    main()
