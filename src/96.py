'''
Created on Apr 18, 2009

@author: anon
'''

import re

def getNextPos(i,j):
    if j == 8:
        i = i + 1
        j = 0
    else:
        j = j + 1
    return((i,j))

def getNextVal(puzzle,i,j,currVal):
    available = set([str(x) for x in range(1,9+1)])
    
    # check row
    row = set([x for x in puzzle[i]])
    row = row.difference(set(['0']))
    
    # check col
    col = []
    for x in puzzle:
        col.append(x[j])        
    col = set(col)
    col = col.difference(set(['0']))
        
    # check square
    square = []
    if i % 3 == 0:
        for x in range(i+0, i+2+1):
            if j % 3 == 0:
                for y in range(j+0, j+2+1):
                    square.append(puzzle[x][y])            
            elif j % 3 == 1:
                for y in range(j-1, j+1+1):
                    square.append(puzzle[x][y])
            elif j % 3 == 2:
                for y in range(j-2, j+1):
                    square.append(puzzle[x][y])
    elif i % 3 == 1:
        for x in range(i-1, i+1+1):
            if j % 3 == 0:
                for y in range(j+0, j+2+1):
                    square.append(puzzle[x][y])            
            elif j % 3 == 1:
                for y in range(j-1, j+1+1):
                    square.append(puzzle[x][y])
            elif j % 3 == 2:
                for y in range(j-2, j+1):
                    square.append(puzzle[x][y])    
    elif i % 3 == 2:
        for x in range(i-2, i+1):
            if j % 3 == 0:
                for y in range(j+0, j+2+1):
                    square.append(puzzle[x][y])            
            elif j % 3 == 1:
                for y in range(j-1, j+1+1):
                    square.append(puzzle[x][y])
            elif j % 3 == 2:
                for y in range(j-2, j+1):
                    square.append(puzzle[x][y])
    square = set(square)
    square = square.difference(set(['0']))
    
    available = available.difference(row)
    available = available.difference(col)
    available = available.difference(square)
    available = available.difference(set([str(x) for x in range(1,int(currVal)+1)]))
    
    available = sorted(list(available))
    
    if len(available) == 0:
        return None
    else:
        return available[0]        

def solvePuzzle(puzzle):
#    print(puzzle)
    # mark which cells are done
    done = []
    for i,row in enumerate(puzzle):
        done.append([])
        for col in row:
            if col == '0':
                done[i].append(False)
            else:
                done[i].append(True)
    
    # now solve it
    locations = []
    currPos = (0,0)
    locations.append((0,0))
    while currPos[0] < 9:
        currPos = locations[-1]
        i = currPos[0]
        j = currPos[1]
#        print(i, j)
        
        if i == 9:
            break
        
        if not done[i][j]:
            nextVal = getNextVal(puzzle, i, j, puzzle[i][j])
        else:
            nextVal = puzzle[i][j]

        if nextVal == None:
            tempRow = [x for x in puzzle[i]]
            tempRow[j] = '0'
            puzzle[i] = ''.join([x for x in tempRow])
            locations.pop()
        else:
            # mark current cell with value and move to next cell
            tempRow = [x for x in puzzle[i]]
            tempRow[j] = nextVal
            puzzle[i] = ''.join([x for x in tempRow])
            
            next = getNextPos(i,j)
            if next[0] == 9:
                break
            while done[next[0]][next[1]]:
                next = getNextPos(next[0],next[1])
                if next[0] == 9:
                    break
            locations.append((next[0],next[1]))

    print(puzzle)

f = open('../sudoku.txt')
r = re.compile('Grid \d\d')
rows = [x.strip() for x in f if r.match(x) == None]

puzzles = []
for i,x in enumerate(rows):
    if i % 9 == 0:
        puzzle = []
    
    puzzle.append(x)
    
    if i % 9 == 8:
        puzzles.append(puzzle)

for puzzle in puzzles:
    solvePuzzle(puzzle)

# TODO: get the sum of topleft 3 numbers of each solved puzzle

print(sum([int(puzzle[0][0:3]) for puzzle in puzzles]))