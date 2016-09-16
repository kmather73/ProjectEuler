# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:22:50 2016

@author: kevin
"""
import PE_Lib

def main():
    count = 0
    for i in range(10**4):
        n = int(str(i)) + int(str(i)[::-1])
        itr = 1
        
        while itr < 50 and not PE_Lib.palindrome(n):
            n = int(str(n)) + int(str(n)[::-1])
            itr += 1
            
        if itr < 50:
            count += 1
            
    print 10**4 - count
    
if __name__ == "__main__":
    main()