#!/usr/python

def main():
    pct = 0.0
    limit = 31080 + 1
    count = 0
    bouncy_count = 0
    n = 1
    while pct < 0.99:
        print(n)
        if isBouncy(n):
            bouncy_count += 1
        count += 1
        pct = float(bouncy_count)/count
        n += 1
    print("*** %d ***" % (n-1))

def isBouncy(x):
    digits = [int(d) for d in str(x)]
    left = 0
    right = len(digits) - 1

    left_max = -1
    right_max = -1

    nonincreasing = False
    nondecreasing = False

    for i in range(len(digits)):
        left_i = digits[left]
        right_i = digits[right]

        if left_i < left_max:
            nonincreasing = True

        if right_i < right_max:
            nondecreasing = True

        if nonincreasing and nondecreasing:
            return True

        if left_i > left_max:
            left_max = left_i

        if right_i > right_max:
            right_max = right_i

        left += 1
        right -= 1

    return False

if __name__ == "__main__":
    main()
