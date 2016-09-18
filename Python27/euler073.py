# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:32:50 2016

@author: kevin
"""


from fractions import Fraction

def main():
    nums = set()
    size = 12000+1

    for d in xrange(1, size):
        for i in range(d/3+1,(d+1)/2):
            x = Fraction(i,d)
            nums.add(x)
        
    
    print len(nums)
if __name__ == "__main__":
    main()