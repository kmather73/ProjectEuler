/* 
 * File:   Problem7.cpp
 * Author: kevin
 *
 * Created on January 8, 2015, 9:49 PM
 */

#include <cstdlib>
#include <iostream>
#include <cmath>

bool IsPrime(long);
const int kLimit=10001;

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {

    long count=2;
    for(int i=0; i < kLimit; ++count){
        if(IsPrime(count)){ 
            i++;
        }
    }
    count -= 1;// need to subtract one since in the final step of the for 
                 // loop we add an extra one.
    cout <<"The " << kLimit << " Prime number is "<< count;
    return 0;
}

bool IsPrime(long num){
    
    for(long i=2;i<=sqrt(num);++i){
        if(num%i==0) return false;
    }
    return true;
}