#!/usr/bin/python

import copy

dim = {'width':-1, 'height':-1}
grid = []
grid_min = []

def load_file():
    global dim
    global grid, grid_min

    f = open('../input/matrix82Test.txt', 'r')
    lines = f.readlines()

    dim['height'] = len(lines)
    dim['width'] = len(lines[0].split(','))

    for i,x in enumerate(lines):
        grid.append([])
        grid_min.append([])
        for j,y in enumerate(x.split(',')):
            grid[i].append(int(y))
            if j == 0:
                grid_min[i].append(int(y))
            else:
                grid_min[i].append(float("INF"))

def inside_grid(row, col):
    global dim
    global grid
    return row >= 0 and col >= 0 and row < dim['height'] and col < dim['width']

def modify_if_necessary(move):
    """ move is row-col pair """
    global grid
    global grid_min
    row,col,name = move
    if inside_grid(row, col):
        if name == 'right':
            sum_to_compare = grid_min[row][col-1] + grid[row][col]
            if sum_to_compare < grid_min[row][col]:
                grid_min[row][col] = sum_to_compare
        elif name == 'right_and_up':
            sum_to_compare = grid_min[row+1][col-1] + grid[row+1][col] + grid[row][col]
            if sum_to_compare < grid_min[row][col]:
                grid_min[row][col] = sum_to_compare
        elif name == 'right_and_down':
            sum_to_compare = grid_min[row-1][col-1] + grid[row-1][col] + grid[row][col]
            if sum_to_compare < grid_min[row][col]:
                grid_min[row][col] = sum_to_compare

def process():
    global dim
    global grid, grid_min

    for row in range(dim['height']):
        for col in range(dim['width']):
            right = (col, row+1, 'right')
            right_and_up = (col-1, row+1, 'right_and_up')
            right_and_down = (col+1, row+1, 'right_and_down')
            moves = [right, right_and_up, right_and_down]
            #print(moves)
            for move in moves:
                modify_if_necessary(move)
    print(grid_min)

def run():
    load_file()
    process()

if __name__ == "__main__":
    run()

