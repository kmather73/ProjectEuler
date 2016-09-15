# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:40:43 2016

@author: kevin
"""
import PE_Lib

def main():
    pentNum = set()
    hexNum = set()
    
    for i in range(10**6):
        pentNum.add(PE_Lib.pentagonalNum(i))
        hexNum.add(PE_Lib.hexagonalNum(i))
        
        
    i = 286
    while PE_Lib.sumUpTo(i) not in pentNum or PE_Lib.sumUpTo(i) not in hexNum:
        i += 1
        
    print PE_Lib.sumUpTo(i)
if __name__ == "__main__":
    main() 