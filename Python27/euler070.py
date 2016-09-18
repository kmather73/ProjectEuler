# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 22:26:09 2016

@author: kevin
"""
import PE_Lib

def main():
    maxQ = 0
    maxN = 0
    for i in range(1, 10**7):
        phi = PE_Lib.phi(i)
        print i
        if sorted(str(phi)) == sorted(str(i)):
            if i/phi > maxQ:
                maxQ = i/phi
                maxN = i
                
    print maxN
    
    
if __name__ == "__main__":
    main()