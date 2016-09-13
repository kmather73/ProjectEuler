# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:05:41 2016

@author: kevin
"""

def main():
    num = ""    
    with open("Files/1000digits.txt", "r") as f:
        for line in f:
            num += line[:-1]
    maxProd = 0    
    for i in range(len(num)-13):
        prod = 1
        for j in range(13):
            prod *= int(num[i+j])
        maxProd = max(prod, maxProd)
        
    print maxProd
    
    
if __name__ == "__main__":
    main()    