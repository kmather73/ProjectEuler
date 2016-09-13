# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:31:20 2016

@author: kevin
"""

import PE_Lib
    
def collatz(n, _d = {1:0}):
    x = n
    length = 1
    while n not in _d:            
        length += 1
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
        
    length += _d[n]
    _d[x] = length
    final = length
    while x != n:
        length -= 1
        _d[x] = length
        if x%2 ==0:
            x = x/2
        else:
            x = 3*x+1
    
    return final

def main(): 
    maxLen = 0
    index = 0
    for i in range(1,10**6):
        currLen = collatz(i)
        
        if currLen > maxLen:
            maxLen = currLen
            index = i
        
    print index
    
    
if __name__ == "__main__":
    main()
