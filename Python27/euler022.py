# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:31:20 2016

@author: kevin
"""

import PE_Lib
    
def points(s):
    score = 0
    for ch in s[1:-1]:
        score += ord(ch)-ord('A')+1

    return score
def main():  
    names = ""
    with open("Files/p022_names.txt", "r") as f:
        for line in f:
            names = line.split(",")
    
    names.sort()
    
    score = 0
    for i in range(len(names)):
        score += (1+i)*points(names[i])
        
    print score
    
if __name__ == "__main__":
    main()
