# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 21:47:56 2016

@author: kevin
"""
from __future__ import division
import PE_Lib

def main():
    maxQ = 0
    maxN = 0
    
    for i in range(2,10**6+1):
        print i
        q = i/PE_Lib.phi(i)
        if q > maxQ:
            maxQ = q
            maxN = i
            
    print maxN
    
    
if __name__ == "__main__":
    main()