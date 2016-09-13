# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:00:54 2016

@author: kevin
"""

import PE_Lib

def main():
    num = 600851475143
    factor = max(PE_Lib.factorize(num))    
    
    print factor
    
if __name__ == "__main__":
    main()