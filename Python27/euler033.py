# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 09:32:00 2016

@author: kevin
"""
from fractions import Fraction

def main():
    prod = Fraction(1)
    for i in range(10,100):
        for j in range(i+1,100):
            i1, i2 = i%10, i/10
            j1, j2 = j%10, j/10
            
            x = False
            x = x or (i1 == j1 and i*j2 == j*i2)
            x = x or (i1 == j2 and i*j1 == j*i2)
            x = x or (i2 == j1 and i*j2 == j*i1)
            x = x or (i2 == j2 and i*j1 == j*i1)
            x = x and i%10 != 0
            
            if x:
                prod *= Fraction(i,j)
                
    print prod.denominator
    
if __name__ == "__main__":
    main()