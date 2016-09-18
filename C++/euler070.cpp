#include <iostream>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;

#include <sstream>

namespace patch{
  template < typename T > std::string to_string( const T& n ) {
    std::ostringstream stm ;
    stm << n ;
    return stm.str() ;
  }
}


int ipow(int base, int exp) {
  int result = 1;
  while(exp) {
    if(exp & 1)
      result *= base;
      exp /= 2;
      base *= base;
  }
  return result;
}

const int MAXN = 10000000;
int phi[MAXN + 1], prime[MAXN/10], sz=0;
vector<bool> mark(MAXN + 1);

void initPhi(){
  phi[1] = 1; 
  for(int i = 2; i <= MAXN; ++i){
    if(!mark[i]){
      phi[i] = i-1;
      prime[sz++]= i;
    }
    
    for(int j=0; j < sz && prime[j]*i <= MAXN; j++ ){
      mark[prime[j]*i] = true;
    
      if(i%prime[j] == 0){
        int ll = 0;
        int xx = i;
        while(xx%prime[j] == 0){
          xx /= prime[j];
          ++ll;         
        }
            
        int mm = ipow(prime[j], ll);
        phi[i*prime[j]] = phi[xx]*mm*(prime[j]-1);
        break;

      } else {
        phi[i*prime[j]] = phi[i]*(prime[j]-1 );
      }
    }
  }
}

int main(){
  initPhi();

  int N = 0;
  double minQ = INT_MAX;

  for(int i=2; i < MAXN; ++i){
    string s1 = patch::to_string(i);
    string s2 = patch::to_string(phi[i]);
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    double q = i/(0.0+phi[i]);
    if( s1 == s2 && q < minQ){
      minQ = q;
      N = i;
    }
  }

  cout << N << endl; 
  return 0;    
} 
