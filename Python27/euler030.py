# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:09:59 2016

@author: kevin
"""
def sumOfDigits(n, k=1):
    tSum = 0
    for ch in str(n):
        tSum += int(ch)**k
    return tSum
    
def main():
    maxRange = 10**7
    tSum = 0
    
    for i in xrange(2, maxRange):
        if i == sumOfDigits(i, 5):
            tSum += i
            
            
    print tSum
    
if __name__ == "__main__":
    main()
