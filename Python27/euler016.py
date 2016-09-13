# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:08:51 2016

@author: kevin
"""

def main():
    tSum = 0    
    for ch in str(2**1000):
        tSum += int(ch)
    print tSum

if __name__ == "__main__":
    main()