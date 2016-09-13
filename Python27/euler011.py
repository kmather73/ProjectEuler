# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:50:24 2016

@author: kevin
"""
def leftFourProd(i, j, grid):
    prod = 1
    if j + 4 < len(grid[0]):
        for k in range(4):
            prod *= grid[i][j+k]
            
    return prod
    
    
def downFourProd(i, j, grid):
    prod = 1
    if i + 4 < len(grid):
        for k in range(4):
            prod *= grid[i+k][j]
            
    return prod
    
def upDiagProd(i, j, grid):
    prod = 1
    if i-4 >= 0 and j+4 < len(grid[0]):
        for k in range(4):
            prod *= grid[i-k][j+k]
    return prod
    
def downDiagProd(i, j, grid):
    prod = 1
    if j-4 > 0 and i+4 < len(grid):
        for k in range(4):        
            prod *= grid[i+k][j-k]
    return prod
    
def main():
    text_file = open("files/largestProduct.txt", "r")
    grid = [[int(n) for n in line.split()] for line in text_file]
    text_file.close()
    
    prod = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            prod = max(prod, downDiagProd(i,j,grid))
            prod = max(prod, upDiagProd(i,j,grid))
            prod = max(prod, leftFourProd(i,j,grid))
            prod = max(prod, downFourProd(i,j,grid))
    print prod
    
    
if __name__ == "__main__":
    main()