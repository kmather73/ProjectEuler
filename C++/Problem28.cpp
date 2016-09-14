/* 
 * File:   Main28.cpp
 * Author: kevin
 *
 * Created on February 4, 2015, 8:18 PM
 * 
 * Here is question 28 of Project Euler.
 * Where we must sum the entries of the diagonals of a spiral of integers that 
 * that starts with one in the middle then we rap the next integers around it
 * until the square formed by it has side length 1001.
 */

#include <cstdlib>
#include <iostream>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int i=1,increment=2;
    int sum=1;
    
    while(i<= 1000*1000){
        for(int j=0;j<4;j++){
            i=i+increment;
            sum=sum+i;            
        }
        increment=increment+2;
    }
    cout<<"The sum of the elements on the diagonal is "<<sum;
    return 0;
}

