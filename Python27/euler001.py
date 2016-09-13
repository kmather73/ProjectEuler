# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 19:37:22 2016

@author: kevin
"""


def sum_3_or_5(limit):
    return sum([x for x in range(limit) if x%3 == 0 or x%5 == 0])

def main():
    limit = 1000
    print( sum_3_or_5(limit) )
    #233168
    
if __name__ == "__main__":
    main()