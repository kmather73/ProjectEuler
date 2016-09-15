# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 21:38:53 2016

@author: kevin
"""   
def main():
    n = 0
    notFound = True    
    
    while notFound:
        n += 1        
        found = True
        for i in range(2,7):
            found = found and sorted(str(n)) ==  sorted(str(i*n))
        
        notFound = not found
        
    print n
    
if __name__ == "__main__":
    main() 