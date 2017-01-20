# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 20:47:21 2017

@author: kevin
"""


import PE_Lib
import math

def pathSum2(grid):
    dp = [[2**127 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
    
    lastCol = len(grid[0])-1
    for row in xrange(len(grid)):
        dp[row][lastCol] = grid[row][lastCol] 
    
    for col in xrange(len(grid[0])-2,-1, -1):
        for _ in range(len(grid[0])):
            for row in xrange(len(grid)):
                cost = grid[row][col]
                if col+1 < len(grid[0]):
                    dp[row][col] = min(dp[row][col], cost + dp[row][col+1])                    
                if row+1 < len(grid):              
                    dp[row][col] = min(dp[row][col], cost + dp[row+1][col])
                if row-1 >= 0:
                    dp[row][col] = min(dp[row][col], cost + dp[row-1][col])
                
    
    leftMin = 2**127
    for i in xrange(len(grid)):
        leftMin = min(leftMin, dp[i][0])
    return leftMin
                
def main():
    grid = PE_Lib.readCSVGrid("Files/p082_matrix.txt")
    print pathSum2(grid)
    
    
if __name__ == "__main__":
    main()