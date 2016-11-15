# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:51:23 2016

@author: kevin
"""
from fractions import Fraction

def main():
    
    x = Fraction(1)
    one = Fraction(1)
    
    count = 0
    for i in range(10**3):
        x = one + one/(x+one)
        
        count += len(str(x.numerator)) > len(str(x.denominator))
            
        
    print count
    
if __name__ == "__main__":
    main()