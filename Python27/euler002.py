# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 19:43:37 2016

@author: kevin
"""

def genFib(limit):
    seq = [1,2]
    i = 1
    
    while seq[i]+seq[i-1] < limit :
        seq.append( seq[i]+seq[i-1])
        i += 1
        
    return seq
def main():
    limit = 4*10**6
    
    seq = genFib(limit)
    tSum = 0
    for x in seq:
        if x%2 == 0:
            tSum += x
            
    print( tSum )
    #233168
    
if __name__ == "__main__":
    main()