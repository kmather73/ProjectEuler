# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:19:17 2016

@author: kevin
"""
def digitSum(n):
    return sum([int(ch) for ch in str(n)])
    
def main():
    tSum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            tSum = max(tSum, digitSum(a**b))
    
    print tSum
    
    
if __name__ == "__main__":
    main()