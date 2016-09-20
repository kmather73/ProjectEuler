# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:24:07 2016

@author: kevin
"""
def isPan(n):
    return len(str(n)) == 10 and len(set(list(str(n)))) == 10
    
def main():    
    print genPan()
    
def sspPan(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    valid = True
    for i in xrange(len(primes)):
        valid = valid and int(str(n)[1+i: 4+i])%primes[i] == 0
        
    return valid
    
def genPan():
    num = [0]*10
    l = genPanUtill(num, 1)
    
    return l
    
def genPanUtill(num, i):
    tSum = 0 
    if i >= len(num):        
        if num[0] != 0 and sspPan(panFromList(num)):
            tSum += panFromList(num)
        return tSum
        
    for j in range(len(num)):
        if num[j] == 0:
            num[j] = i
            tSum += genPanUtill( num, i+1)
            num[j] = 0
    
    return tSum
def panFromList(l):
    tSum = 0
    prod = 1
    for i in reversed(range(len(l))):
        tSum += prod * l[i]
        prod *= 10
        
    return tSum
        
if __name__ == "__main__":
    main()