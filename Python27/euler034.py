# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:09:59 2016

@author: kevin
"""
from math import factorial

def digitFactSum(n):
    tSum = 0
    for ch in str(n):
        tSum += factorial(int(ch))
    return tSum
    
def main():
    maxRange = 10**7
    tSum = 0
    
    for i in xrange(3, maxRange):
        if i == digitFactSum(i):
            tSum += i
            
            
    print tSum
    
if __name__ == "__main__":
    main()
    
    
    #umdevclub
