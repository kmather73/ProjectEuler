# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:31:20 2016

@author: kevin
"""

import PE_Lib
    

def main():  
    abudant = set()
    for i in range(1,28124):
        if PE_Lib.sigma1(i) > 2*i:
            abudant.add(i)
        
        
    nums = set()
    for x in abudant:
        for y in abudant:
            nums.add(x+y)
            
            
    print sum([x for x in range(1, 28124) if x not in nums])
    
    
if __name__ == "__main__":
    main()
