# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:43:23 2016

@author: kevin
"""

def main():
    sz = 1000    
    maxLen = 0
    maxD = 0
    for i in range(1, sz+1):
        d = {}
        currLen = 0
        r = 1
        while r not in d:
            currLen += 1
            d[r] = currLen
            r *= 10
            r = r%i
            
        if currLen-d[r] > maxLen:
            maxLen = currLen-d[r]
            maxD = i

    print maxD, maxLen
    
if __name__ == "__main__":
    main()