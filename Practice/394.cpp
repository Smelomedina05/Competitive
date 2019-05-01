#include <iostream>
#include <map>
#include <vector>
using namespace std;

struct Array{
  int base;
  int bytes;
  int dimensions;
  int c0;
  vector<int> lw;
  vector<int> up;
  int cts[100];
  void reset(){
    lw.clear();
    up.clear();
    c0 = 0;
  }
};

void medium(Array &a){
  for (int n = a.dimensions-1; n > 0; n--)
    a.cts[n] = a.cts[n+1] * (a.up.at(n+1)-a.lw.at(n+1)+1);

  for (int n = 1; n <= a.dimensions; n++)
    a.cts[0] -= a.cts[n] * a.lw.at(n);
}

int main(){
  int a, r, tmp, tmp2;
  cin >> a >> r;
  map<string, Array> m;
  vector<int> entrada;
  string name;
  Array array;
  while(a--){
    array.lw.push_back(0);
    array.up.push_back(0);
    cin >> name;
    cin >> array.base >> array.bytes >> array.dimensions;
    array.cts[0] = array.base;
    array.cts[array.dimensions] = array.bytes;
    for (int n = 0; n < array.dimensions; n++){
      cin >> tmp >> tmp2;
      array.lw.push_back(tmp);
      array.up.push_back(tmp2);
    }
    medium(array);
    m.insert({name, array});
    array.reset();
  }
  while(r--){
    entrada.push_back(0);
    cin >> name;
    tmp2 = m[name].cts[0];
    cout << name << "[";
    for (int n = 1; n <= m[name].dimensions; n++){
      cin >> tmp;
      if (n != m[name].dimensions) cout << tmp << ", ";
      tmp2 += tmp * m[name].cts[n];
    }
    cout << tmp << "] = ";
    cout << tmp2 << endl;
  }
  return 0;
}
