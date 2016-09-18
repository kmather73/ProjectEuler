# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 17:06:04 2016

@author: kevin
"""
def main():
    sz = 200    
    dp = [0]*(sz + 1)
    dp[0] = 1
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    
    for coin in coins:
        for i in range(coin,sz+1):
            dp[i] += dp[i-coin]
    
    print dp[sz]

if __name__ == "__main__":
    main()