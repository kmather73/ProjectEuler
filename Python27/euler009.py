# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:12:21 2016

@author: kevin
"""
from functools import reduce
from operator import mul

def PythagoreanTripls(u,v):
    if v > u:
        u, v = v, u
    return [2*u*v, u**2 - v**2, u**2+v**2]

def main():
    for i in range(1, 1000):
        for j in range(1,1000):
            l = PythagoreanTripls(i,j)
            if sum(l) == 1000:
                print reduce(mul, l)
                
    
    
    
if __name__ == "__main__":
    main()