/* 
 * File:   Problem10.cpp
 * Author: kevin
 *
 * Created on January 11, 2015, 5:00 PM
 */

#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;
bool IsPrime(int);

const int kLimit=2000000;
/*
 * 
 */
int main(int argc, char** argv) {
    long long sum=2;
    for(int i=3;i<kLimit; i+=2)
        if(IsPrime(i))
            sum+=i;
    
    cout<<"The sum of primes less than "<< kLimit<< " is "<<sum;
    return 0;
}

bool IsPrime(int num){
    if(num<3) return true;
    for(int i=2;i<=sqrt(num);i++)
        if((num%i)==0)return false;
    
    return true;
}