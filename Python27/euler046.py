# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 08:35:30 2016

@author: kevin
"""
import PE_Lib

def main():
    i = 3
    squares = [x**2 for x in xrange(10**3)]
    condition = True
    
    while condition:
        s = 0
        found = False
        while 2*squares[s] < i and not found:
            p = 0
            while 2*squares[s] + PE_Lib._known_primesList[p] <= i:
                if 2*squares[s] + PE_Lib._known_primesList[p] == i:
                    found = True
                p += 1
            s += 1
        i += 2
        condition = found
                    
    print i-2
    
if __name__ == "__main__":
    main()