# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 07:50:04 2016

@author: kevin
"""
import PE_Lib

def main():
    condition = True
    num = 4    
    
    i = 2
    while condition:
        factors= [set(PE_Lib.factorize(i+k)) for k in range(num)]
        valid = all([len(x) == num for x in factors])
        
        for j in range(num-1):
            valid = valid and len(factors[j] & factors[j+1]) == 0
        
        condition = not valid
        
        i += condition
        
    print i
    
if __name__ == "__main__":
    main()