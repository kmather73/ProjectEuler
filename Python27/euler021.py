# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:05:20 2016

@author: kevin
"""
import PE_Lib

def main():
    d = {}    
    for i in range(1,10000):
        d[i] = PE_Lib.sigma1(i)-i
    
    
    amicable = set()
    for i in d:
        for j in d:
            if i != j and d[i] == j and d[j] == i:
                amicable.add(i)
                amicable.add(j)
        
    print sum(amicable)
if __name__ == "__main__":
    main()