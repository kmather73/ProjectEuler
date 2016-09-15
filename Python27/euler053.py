# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:00:18 2016

@author: kevin
"""
import PE_Lib

def main():
    count = 0    
    for n in range(1, 101):
        for k in range(1, n):        
            if PE_Lib.nCk(n,k) > 10**6:
                count += 1
            
    print count
if __name__ == "__main__":
    main()