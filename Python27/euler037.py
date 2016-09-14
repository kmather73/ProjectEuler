# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:09:24 2016

@author: kevin
"""

import PE_Lib

def rightPrimes(n):
    rPrime = True
    while n > 0 and rPrime:
        
        rPrime = rPrime and PE_Lib.isPrime(n)
        n = int("0"+str(n)[:-1])
    return rPrime
    
def leftPrimes(n):
    lPrime = True
    while n > 0 and lPrime:
        
        lPrime = lPrime and PE_Lib.isPrime(n)
        n = int("0"+str(n)[1:])
    return lPrime

def main():
    nums = []
    i = 10
    while len(nums) < 11:
        if PE_Lib.isPrime(i) and leftPrimes(i) and rightPrimes(i):
            nums.append(i)
        i += 1
        
            
    print nums
    print sum(nums)
            
    
if __name__ == "__main__":
    main() 