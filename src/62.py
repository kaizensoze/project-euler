#!/usr/python

import itertools

# apparently very slow, only got to 870 so far; maybe generate all cubes ahead of time?
def main():
    x = 345
    while True:
        x3 = x**3
        all_cubes = set([])
        cube_results = set([])
        perms = list(itertools.permutations([p for p in str(x3)]))
        clean_perms = [int(''.join(p)) for p in perms if p[0] != '0']
        for perm in [cp for cp in clean_perms]:
            if perm in all_cubes:
                cube_check = True
            else:
                cube_check = round(perm ** (1.0/3)) ** 3 == perm
            if cube_check:
                cube_results.add(perm)
                all_cubes.add(perm)
        if len(cube_results) == 5:
            print("*** FOUND IT (x = %s) ***" % x)
            print(cube_results)
            return
        x += 1
        print(x)

if __name__ == "__main__":
    main()
