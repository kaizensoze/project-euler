
dim = [0, 0]
i = 1

curr = [complex(0,0)]

DOWN = complex(1,0)
RIGHT = complex(0,1)

d = {}
mins = {}

def load():
    global dim

    f = open('../matrix81.txt', 'r')
    lines = f.readlines()

    dim[0] = len(lines)
    dim[1] = len(lines[0].split(','))

    for i,x in enumerate(lines):
        for j,y in enumerate(x.split(',')):
            d[complex(i,j)] = int(y)

def moveOut(pos):
    global curr, d, DOWN, RIGHT, i

    if i % 2 == 0:
        next1 = pos + DOWN
        next2 = pos + RIGHT
    else:
        next1 = pos + RIGHT
        next2 = pos + DOWN

    if next1 in d:
        curr.append(next1)
    if next2 in d:
        curr.append(next2)

    i += 1

def prev(pos, action):
    return pos + -1*action

def step(pos):
    global d, mins, RIGHT, DOWN, i

    posL = prev(pos, RIGHT)
    posU = prev(pos, DOWN)
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
    
    if posU_val is None and posL_val is None:
        minVal = val
    elif posU_val is None:
        minVal = val + posL_val
    elif posL_val is None:
        minVal = val + posU_val
    else:
        minVal = min(val + posL_val, val + posU_val)

    mins[pos] = minVal

    moveOut(pos)

def run():
    global dim, curr

    load()

    while len(curr) > 0:
        print(curr)
        c = curr.pop(0)
        if c not in mins:
            step(c)

    endPos = complex(dim[0]-1,dim[1]-1)
    #print(mins)
    print(mins[endPos])

run()
