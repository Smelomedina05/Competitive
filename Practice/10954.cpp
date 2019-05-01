#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

struct Counter{
  int deliver = 0;
  int two = 100000;
  void add(int n, map<int, int> &m){
    if (n != 2147483647)
      if (two == 100000) {two = n;}
      else {
        deliver+=n+two;
        if (m.find(n+two) != m.end()) m[n+two] = m[n+two] + 1;
        else m.insert({n+two, 0});
        two = 100000;
      }
    else
      if (two == 100000) {two = 0;}
      else {
        deliver+=m.begin()->first;
        two = 100000;
      }
  }
  void reset(){
    deliver = 0;
    two = 100000;
  }
};

int main(){
  Counter c;
  int t, cs, tmp;
  map<int, int> m;
  map<int, int>::iterator it;
  cin >> t;
  while (t > 0){
    while (t--){
      cin >> cs;
      if (cs != 0)
        if (m.find(cs) != m.end()) m[cs] = m[cs] + 1;
        else m.insert({cs, 0});
      else
        m.insert({2147483647, 0});
    }
    for (it = m.begin(); it != m.end(); it++)
      if (it->second != 0)
        for (int n = 0; n <= it->second; n++)
          c.add(it->first, m);
      else
        c.add(it->first, m);
    cout << c.deliver << endl;
    c.reset();
    m.clear();
    cin >> t;
  }
  return 0;
}
