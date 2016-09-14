# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:31:15 2016

@author: kevin
"""
def main():
    digits, num = 0, 0
    prod = 1
    nums = [10**i for i in range(0,7)]
    
    while digits < 10**6+1:
        num += 1
        for ch in str(num):
            digits += 1
            if digits in nums:
                prod *= int(ch)
    print prod
if __name__ == "__main__":
    main() 
