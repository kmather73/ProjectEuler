# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:57:44 2016

@author: kevin
"""
import PE_Lib 

def points(s):
    score = 0
    for ch in s[1:-1]:
        score += ord(ch)-ord('A')+1

    return score
    
def main():
    triNums = set([ PE_Lib.sumUpTo(i) for i in range(2000)])
    count = 0
    
    with open("Files/p042_words.txt", "r") as f:
        for line in f:
            names = line.split(",")
            for i in range(len(names)):
                if points(names[i]) in triNums:
                    count += 1
    print count
if __name__ == "__main__":
    main() 