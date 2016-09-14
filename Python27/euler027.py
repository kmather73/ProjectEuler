# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:52:42 2016

@author: kevin
"""
import PE_Lib
import math
def consecutivePrimes(fun):
    i = 0
    while PE_Lib.isPrime(int(math.fabs(fun(i)))):
        i += 1
        
    return i
    
    
def main():
    maxRun = 0
    maxProd = 0
    
    for a in range(-999, 1000, 1):
        for b in range(-999, 1000, 1):
            f = lambda x : x**2 + a*x + b
            temp = consecutivePrimes(f)
            
            if temp > maxRun:
                maxRun = temp
                maxProd = a*b
            elif temp == maxRun:
                maxProd = max(maxProd, a*b)
                
                
    print maxProd
                
            
    
if __name__ == "__main__":
    main()