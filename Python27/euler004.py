# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:05:35 2016

@author: kevin
"""

def isPal( num ):
    return str(num) == str(num)[::-1]
    
    
    
    
def main():
    maxNum = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if isPal(i*j):
                maxNum = max(maxNum, i*j)
    print "max pal is", maxNum
if __name__ == "__main__":
    main()