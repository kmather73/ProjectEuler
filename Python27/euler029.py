# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 23:09:59 2016

@author: kevin
"""

def main():
    nums = set()
    
    for a in range(2,101):
        for b in range(2,101):
            nums.add(a**b)
            
            
    print len(nums)
    
if __name__ == "__main__":
    main()