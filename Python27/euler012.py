# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:31:20 2016

@author: kevin
"""

import PE_Lib
    
   
def main():
    i = 1;    
    while PE_Lib.sigma0(PE_Lib.sumUpTo(i)) <= 500:
        i += 1
    print PE_Lib.sumUpTo(i)
    
if __name__ == "__main__":
    main()