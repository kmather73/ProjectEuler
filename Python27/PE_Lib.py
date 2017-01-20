# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:29:55 2016

@author: kevin
"""

from fractions import gcd
from functools import reduce
from collections import defaultdict
from math import factorial
from math import sqrt
from math import exp
from math import log
import random
import string
 
#------------------------------------------------------------------------------
# Number Theory functions
#------------------------------------------------------------------------------
 
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

def lcmm(args):
	"""Compute the lowest common multiple of [a,b,c,...]"""
	return reduce(lcm, args)

def gcdd(args):
	"""Compute the greatest common divisors of [a,b,c,...]"""
	return reduce(gcd, args)


def nCk(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))


def genPentagonalNum(n):
    """Compute the nth Pentagonal number"""
    return n*(3*n-1)/2 + (1-n)*(3*(1-n)-1)/2
    
def pentagonalNum(n):
    """Compute the nth Pentagonal number"""
    return n*(3*n-1)/2
    
def hexagonalNum(n):
    """Compute the nth Hexagonal number"""
    return n*(2*n-1)
    
def sumOfSquares(n):
    """Compute the sum of squares of the first n integers"""
    return n*(n+1)*(2*n+1)/6
    
def sumUpTo(n):
    """Compute the sum of the first n integers"""
    return n*(n+1)/2

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite

def isPrime(n, _precision_for_huge_n=16):
    ''' Returns True if n is a prime number '''
    # This is the so called RabinMiller prime factorization
    if n in (0, 1):
        return False
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])

def sieveAndPhi(n):
    s = [False] * (n + 1)
    phi = [0]*(n + 1)
    primes = []
    phi[1] = 1
    
    for i in range(2, n):
        if not s[i]:
            phi[i] = i-1
            primes.append(i)
        
        
        j = 0
        while j < len(primes) and primes[j]*i < n:
            s[primes[j]*i] = True
            
            if i % primes[j] == 0:
                ppow = 1
                num = i
                while num%primes[j] == 0:
                    ppow *= primes[j]
                    num /= primes[j]
                    
                phi[int(i*primes[j])] = phi[int(num)] * ppow * (primes[j] - 1)
                break
            else:
                phi[i*primes[j]] = phi[i]*(primes[j]-1)
            
            j += 1
            
    return primes, phi
    
#_known_primes = [2, 3]
#_known_primes += set([x for x in range(5, 50000, 2) if isPrime(x)])
_tblSize = 10**6
_known_primesList, _phi = sieveAndPhi(_tblSize)
_known_primes = set(_known_primesList)

def brentFactorisation(n): 
    """Try to find a non-trival factor of n"""
    # http://maths-people.anu.edu.au/~brent/pd/rpb051i.pdf
    # http://connellybarnes.com/documents/factoring.pdf
    # http://mathworld.wolfram.com/BrentsFactorizationMethod.html
    x=0
    y=0
    ys=0
    a=0
    m = 1000
    
    while a == 0 or a == n-2:
        a = random.randint(0,n-1)
        
    y = random.randint(0,n-1)
    r = 1
    q = 1
    g = 1
    
    while g == 1:
        x = y
        for i in range(r):
            y = (y**2 + a) % n
        k = 0
        
        while(k < r and g == 1):
            for i in range(min(m, r-k)):
                ys = y
                y = (y**2 + a) % n
                q = q*abs(x-y) % n
            
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        condition = True
        while condition:
            ys = (ys**2 + a) % n
            g = gcd(abs(x-ys), n)
            condition = g==1
            
    return g

def factorize(n, _d={0: [], 1: [], 2: [2]}):
    '''Returns a list of prime factors of n, a factor p will appear multiple times in the list according to its multiplicity'''
    args = n
    if n in _d:
        return _d[n]
    factors = []
    while n != 1:
        q = brentFactorisation(n)
        n //= q
        if isPrime(q):
            factors += [q]
        else:
            factors += factorize(q)
        if n in _d:
            factors += _d[n]
            break
    _d[args] = factors
    return factors

def phi(n):
    '''Returns the euler totient of an integer'''
    # This pure integer solution avoids the loss of precison that comes with
    # dealing 1/p
    if n < _tblSize:
        return _phi[n]
        
    primes = factorize(n)
    n = 1
    for p in set(primes):
        n *= p ** (primes.count(p) - 1) * (p - 1)
    return n
    

    
def PythagoreanTripls(u,v):
    if v > u:
        u, v = v, u
    return [2*u*v, u**2 - v**2, u**2+v**2]
    
def sigma0(n):
    l = factorize(n)
    m = defaultdict(int)
    for x in l:
        m[x] += 1
    
    sigma = 1        
    for k in m:
        sigma *= (1+m[k])
    return sigma

def sigma1(n):
    tSum = 0
    for i in range(1, int(sqrt(n)+1)):
        if n%i == 0:
            tSum += (i + (n/i))
            
    if n == int(sqrt(n))**2:
        tSum -= int(sqrt(n))
    return tSum
    
def sigmaK2(n,k):
    sigma = 1
    
    i = 0
    while n >= _known_primesList[i]:
        x = _known_primesList[i]**k        
        j = 1
        tSum = 1
        while n%_known_primesList[i] == 0:
            n /= _known_primesList[i]            
            j *= x
            tSum += j
        sigma *= tSum
        i += 1
    return sigma
    
def sigmaK(n, k):
    l = factorize(n)
    m = defaultdict(int)
    for x in l:
        m[x] += 1
    
    sigma = 1      
    for x in m:
        sigma *= (x**(k*(m[x]+1))-1)/(x**k-1)
    return sigma
               
def generateFactors(n, primes, start=1, factors=(), genOne=False):
    '''This generates a list of all factors of n with numbers between 1 and n'''
    if genOne:
        yield (1,)
    if start <= n:
        for a in primes[start:n]:
            yield factors + (a,)
            for c in generateFactors(n // a, primes, a, factors + (a,)):
                yield c
#------------------------------------------------------------------------------
# String functions
#------------------------------------------------------------------------------
 
def palindrome(n):
    """Determines if a number is a palindrone"""
    return (str(n))[::-1] == str(n)


    
digs = string.digits + string.ascii_letters
def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)
  
  
  
def validPair(i,j, primes):
    return isPrime(int(str(primes[i])+str(primes[j]))) and isPrime(int(str(primes[j])+str(primes[i])))

def Q60(limit):
    primes = []
    i = 2
    
    while len(primes) < limit:
        if isPrime(i):                                     
            primes.append(i)
        i += 1        
        
    n = len(primes)
    for i1 in range(n):
        for i2 in range(i1+1, n):
            if validPair(i1, i2, primes):
                for i3 in range(i2+1, n):
                    if validPair(i1, i3, primes) and validPair(i2, i3, primes):
                        for i4 in range(i3+1, n):
                            if validPair(i1, i4, primes) and validPair(i2, i4, primes) and validPair(i3, i4, primes):
                                for i5 in range(i4+1, n):
                                    if validPair(i1, i5, primes) and validPair(i2, i5, primes) and validPair(i3, i5, primes) and validPair(i4, i5, primes):
                                        print( sum([primes[x] for x in [i1, i2, i3, i4, i5]]))
                                        
                                        
#------------------------------------------------------------------------------
# Preprocessing functions
#------------------------------------------------------------------------------
def readCSVGrid(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            grid.append([])
            for num in line.split(","):
                grid[-1].append(int(num))
                
    return grid