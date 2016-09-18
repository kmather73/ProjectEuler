# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 18:30:47 2016

@author: kevin
"""
import PE_Lib

def fareySequence(n):
    tSum = 0
    for i in xrange(2,n+1):
        tSum += PE_Lib.phi(i)
        
    return tSum
    
    
def main():
    print fareySequence(10**6)
    
    
if __name__ == "__main__":
    main()