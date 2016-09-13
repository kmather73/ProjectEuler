# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:31:20 2016

@author: kevin
"""

import PE_Lib
    
   
def main():  
    tSum = 0
    with open("Files/number.txt", "r") as f:
        for num in f:
            tSum += int(num)
    print tSum
if __name__ == "__main__":
    main()
