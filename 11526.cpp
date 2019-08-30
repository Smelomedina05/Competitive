#include <iostream>
#include <math.h>
using namespace std;

long long H(long long n){
  long long num = 0;
  int limit = sqrt(n);
  for(int m = 1; m <= limit; m++){
    num += 2*(n/m);
  }
  return num-limit*limit;
}

int main(){
  int t;
  long long cs;
  cin >> t;
  while (t--){
    cin >> cs;
    cout << H(cs) << endl;
  }
  return 0;
}
