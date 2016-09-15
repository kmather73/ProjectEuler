# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:49:59 2016

@author: kevin
"""
def main():
    tSum = 0
    for i in range(1,1001):
        tSum = (tSum + i**i) % 10**10
        
    print tSum

if __name__ == "__main__":
    main() 