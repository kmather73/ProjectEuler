# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:45:56 2016

@author: kevin
"""

import PE_Lib
from math import sqrt 

def main():
    maxSize = 0
    pMax = 0    
    
    for p in range(12,1001):
        sol = set()
        for u in range(1,1001):
            for v in range(u+1,int(sqrt(max(0,1001-u**2)))):
               trip = PE_Lib.PythagoreanTripls(u,v)
               
               if p % sum(trip) == 0:
                    r = p/sum(trip)                   
                    sol.add(tuple( [x*r for x in trip]) )
               

        if len(sol) > maxSize:
            maxSize = len(sol)
            pMax = p
            
            
    print pMax
    
if __name__ == "__main__":
    main() 