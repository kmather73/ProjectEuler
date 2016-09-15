# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 21:09:15 2016

@author: kevin
"""
import PE_Lib

def main():
    nums = []
    for a in range(1000, 10000):
        
        for d in range(2,1+(10000-a)//2, 2):
            valid = True
            for n in range(3):
                valid = valid and PE_Lib.isPrime(a + n*d)
                
            if valid and sorted(str(a)) == sorted(str(a+d)) == sorted(str(a+2*d)):
                nums.append( [a+i*d for i in range(3)] )
    print nums
    
if __name__ == "__main__":
    main() 