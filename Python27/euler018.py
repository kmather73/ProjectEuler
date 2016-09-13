# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:10:48 2016

@author: kevin
"""

def maxTriPath(tri):
    dp = [[0]*len(row) for row in tri]
    dp[0][0] = tri[0][0]
    
    row = 1
    col = 0
    for row in range(1,len(tri)):
        dp[row][0] = tri[row][0] + dp[row-1][0]
        dp[row][-1] = tri[row][-1] + dp[row-1][-1]
        for col in range(1,len(tri[row])-1):
            dp[row][col] = max(dp[row-1][col], dp[row-1][col-1])+tri[row][col]
    return max(dp[-1])
    
def main():
    triangle = []    
    with open("Files/triangle.txt", "r") as f:
        for line in f:
            l = []
            for num in line.split():
                l.append(int(num))
            triangle.append(l)
            
    print maxTriPath(triangle)
if __name__ == "__main__":
    main()