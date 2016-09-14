# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:57:26 2016

@author: kevin
"""
from math import factorial
def main():
    num = str(factorial(100))
    
    tSum = 0
    for ch in num:
        tSum += int(ch)
    
    print tSum
if __name__ == "__main__":
    main()