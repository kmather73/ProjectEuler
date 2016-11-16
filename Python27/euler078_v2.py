# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:42:00 2016

@author: kevin
"""

import PE_Lib
import math

def coins():
    million = 1000000
    dp = [1]
    n = 0
    
    while dp[-1] != 0 or n == 0:
        n += 1        
        if n% 10000 == 0:
            print n

        i = 0        
        pen = 1
        dp.append(0)
        while pen <= n:
            sign = 1
            if i%4 > 1:
                sign = -1
            

            dp[n] += sign * dp[n-pen]
            dp[n] = dp[n] % million
            i += 1
        
            j = i/2+1
            
            if i%2 != 0:
                j = -j
                
            pen = PE_Lib.pentagonalNum(j)
        
        

    return n


def main():
    
    print coins()
    
    
if __name__ == "__main__":
    main()