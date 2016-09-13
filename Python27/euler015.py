# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:02:45 2016

@author: kevin
"""
from math import factorial

def nCk(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

def main():
    print nCk(40,20)
   
if __name__ == "__main__":
    main()
