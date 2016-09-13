# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:17:03 2016

@author: kevin
"""

def sumOfSquares(n):
    return n*(n+1)*(2*n+1)/6
    
def sumUpTo(n):
    return n*(n+1)/2
    
def main():
    x = 100    
    print sumUpTo(x)**2 - sumOfSquares(x)
if __name__ == "__main__":
    main()