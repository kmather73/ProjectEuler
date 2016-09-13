# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:13:14 2016

@author: kevin
"""

from fractions import gcd
from functools import reduce
 
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

def lcmm(args):
	"""Compute the lowest common multiple of [a,b,c,...]"""
	return reduce(lcm, args)

def gcdd(args):
	"""Compute the greatest common divisors of [a,b,c,...]"""
	return reduce(gcd, args)


def main():
    print lcmm(range(1,21))
    
    
    
if __name__ == "__main__":
    main()