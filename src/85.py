#!/usr/python

def main():
    """
    m=3,n=2
    mxn (3x2) (in this case m=width,n=height)
    
    i=1..n
        j=1..m
            num_rects = (m-(j-1)) * (n-(i-1))

    i=1,j=1 => 3-0 * 2-0 = 6
    i=1,j=2 => 3-1 * 2-0 = 4
    i=1,j=3 => 3-2 * 2-0 = 2
    i=2,j=1 => 3-0 * 2-1 = 3
    i=2,j=2 => 3-1 * 2-1 = 2
    i=2,j=3 => 3-2 * 2-1 = 1
    """
    goal = 2000000
    pad = 15
    num_rects = 0

    for m in range(1,999):
        for n in range(1,999):
            num_rects = 0
            for i in range(1,n+1):
                for j in range(1,m+1):
                    num_rects += (m-(j-1)) * (n-(i-1))
            if (num_rects >= (goal-pad) and num_rects <= goal) or (num_rects >= goal and num_rects <= (goal+pad)):
                print(m*n, num_rects)
                return

if __name__ == "__main__":
    main()
