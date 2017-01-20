# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 20:24:55 2017

@author: kevin
"""


import PE_Lib
import math

def rightDownPathSum(grid, row, col, _dp = {}):
    if row == len(grid)-1 and col == len(grid[0])-1:
        return grid[row][col]
    elif row >= len(grid) or col >= len(grid[0]):
        return 2**127
    elif (row, col) in _dp:
        return _dp[(row,col)]
        
    right = rightDownPathSum(grid, row, col+1, _dp)
    down = rightDownPathSum(grid, row+1, col, _dp)
    
    best = min(right, down) + grid[row][col]
    _dp[(row, col)] = best
    return best

def readGrid(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            grid.append([])
            for num in line.split(","):
                grid[-1].append(int(num))
                
    return grid
                
def main():
    grid = readGrid("Files/p081_matrix.txt")
    print rightDownPathSum(grid,0, 0)
    
    
if __name__ == "__main__":
    main()