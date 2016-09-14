# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:09:59 2016

@author: kevin
"""
import PE_Lib

def isCircular(n):
    circ = True
    n = str(n)
    for i in range(len(n)):
        circ = circ and PE_Lib.isPrime(int(n))
        n = str(n)[1:]+str(n)[0]
        
    return circ


def main():
    maxRange = 10**6
    tSum = 0
    
    for i in xrange(2, maxRange):
        if isCircular(i):
            tSum += 1
                
    print tSum
    
if __name__ == "__main__":
    main()
    
