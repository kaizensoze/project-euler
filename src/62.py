#!/usr/python

def main():
    start = 999
    end = 9999+1
    num_perms_looking_for = 5
    cubes = set([x**3 for x in range(start, end)])

    for p in cubes:
        cube_results = set([p])
        for q in cubes:
            if p != q and isPalindrome(p, q):
                cube_results.add(q)
        if len(cube_results) == num_perms_looking_for:
            print("*** FOUND IT (%s) ***" % p)
            print(sorted(cube_results))
            return

def isPalindrome(x, y):
    # expected: x,y are ints
    return sorted([a for a in str(x)]) == sorted([b for b in str(y)])

if __name__ == "__main__":
    main()
