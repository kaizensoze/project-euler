
dim = [0, 0]
i = 0

curr = [complex(0,0)]

UP = complex(-1,0)
DOWN = complex(1,0)
RIGHT = complex(0,1)

d = {}
mins = {}

def load():
    global dim

    f = open('../matrix82Test.txt', 'r')
    lines = f.readlines()

    dim[0] = len(lines)
    dim[1] = len(lines[0].split(','))

    for i,x in enumerate(lines):
        for j,y in enumerate(x.split(',')):
            d[complex(i,j)] = int(y)

def moveOut(pos):
    global curr, d, UP, DOWN, RIGHT, i

    if pos.imag == dim[1] - 1:
        return

    if i % 3 == 0:
        next1 = pos + UP
        next2 = pos + DOWN
        next3 = pos + RIGHT
    elif i % 3 == 1:
        next1 = pos + RIGHT
        next2 = pos + DOWN
        next3 = pos + UP
    else:
        next1 = pos + DOWN
        next2 = pos + RIGHT
        next3 = pos + UP

    if next1 in d:
        curr.append(next1)
    if next2 in d:
        curr.append(next2)
    if next3 in d:
        curr.append(next3)

    i += 1

def prev(pos, action):
    return pos + -1*action

def step(pos):
    global d, mins, UP, RIGHT, DOWN, i

    posD = prev(pos, UP)
    posL = prev(pos, RIGHT)
    posU = prev(pos, DOWN)

    if posD in d:
        if posD in mins:
            posD_val = mins[posD]
        else:
            posD_val = d[posD]
    else:
        posD_val = None

    if posL in d:
        if posL in mins:
            posL_val = mins[posL]
        else:
            posL_val = d[posL]
    else:
        posL_val = None

    if posU in d:
        if posU in mins:
            posU_val = mins[posU]
        else:
            posU_val = d[posU]
    else:
        posU_val = None

    val = d[pos]

    # DLU
    # 000
    # 001
    # 010
    # 100
    # 011
    # 101
    # 110
    # 111
    
    if posD_val is None and posL_val is None and posU_val is None:
        minVal = val
    elif posD_val is None and posL_val is None:
        minVal = val + posU_val
    elif posD_val is None and posU_val is None:
        minVal = val + posL_val
    elif posL_val is None and posU_val is None:
        minVal = val + posD_val
    elif posD_val is None:
        minVal = min(val + posL_val, val + posU_val)
    elif posL_val is None:
        minVal = min(val + posD_val, val + posU_val)
    elif posU_val is None:
        minVal = min(val + posD_val, val + posL_val)
    else:
        minVal = min(val + posU_val, val + posL_val, val + posU_val)

    mins[pos] = minVal

    moveOut(pos)

def run():
    global dim, curr

    load()

    while len(curr) > 0:
        c = curr.pop(0)
        if c not in mins:
            print(curr)
            step(c)

    endPos = complex(dim[0]-1, dim[1]-1)
    res = 9999999999999999999999
    for x in range(dim[0]):
        if mins[complex(x,dim[1]-1)] < res:
            res = mins[complex(x,dim[1]-1)]
    print(res)

run()
