# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:17:44 2016

@author: kevin
"""

from fractions import Fraction

def main():
    num = set()
    size = 10**6+1
    x = Fraction(3,7)
    num = 0
    
    for d in xrange(1, size):
        y = Fraction(1,7*d)
        diff = x-y
        if diff.denominator < size:
            num = diff.numerator
    
    print num
if __name__ == "__main__":
    main()