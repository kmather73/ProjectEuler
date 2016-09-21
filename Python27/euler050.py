# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 08:03:05 2016

@author: kevin
"""
import PE_Lib

def main():
    primeSum = [0]
    
    for i in xrange(len(PE_Lib._known_primesList)):
        primeSum.append( primeSum[i] + PE_Lib._known_primesList[i])
        
    maxLen = 0
    maxPrime = 0
    
    for i in range(len(primeSum)):
        for j in range(i+maxLen+1, len(primeSum)):
            
            pSum = primeSum[j]-primeSum[i]
            if pSum in PE_Lib._known_primes and j-i > maxLen:
                maxLen = j-i
                maxPrime = pSum
            elif pSum > PE_Lib._known_primesList[-1]:
                break
    print maxPrime
    
if __name__ == "__main__":
    main()