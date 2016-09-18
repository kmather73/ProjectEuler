# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:29:16 2016

@author: kevin
"""

import PE_Lib
def primePartion(n):
    dp = [0]*(n+1)
    dp[0] = 1
    
    i = 0
    while PE_Lib._known_primesList[i] <= n:
        p = PE_Lib._known_primesList[i]
        for j in range(p, n+1):
            dp[j] += dp[j-p]
            
        i += 1
    return dp[n]

def main():
    i = 2    
    size = 5000
    
    while primePartion(i) < size:
        i += 1
        
    print i
    
    
if __name__ == "__main__":
    main()    