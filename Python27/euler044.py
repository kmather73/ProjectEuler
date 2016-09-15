# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 19:13:01 2016

@author: kevin
"""
import PE_Lib

def main():
    penNums = set()
    
    for i in xrange(1,10000):
        penNums.add(PE_Lib.pentagonalNum(i))
        
        
    minDist = 2**31
    
    for a in penNums:
        for b in penNums:
            if abs(a-b) in penNums and a+b in penNums and abs(a-b) < minDist:
                minDist = abs(a-b)
                
    print minDist

if __name__ == "__main__":
    main() 