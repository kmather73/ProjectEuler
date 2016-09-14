# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:01:31 2016

@author: kevin
"""
import PE_Lib

def main():
    tSum = 0    
    for i in xrange(1, 10**6):
        if PE_Lib.palindrome(i) and PE_Lib.palindrome(PE_Lib.int2base(i,2)):
            tSum += i
            
    print tSum
    
if __name__ == "__main__":
    main()    