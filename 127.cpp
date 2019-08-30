#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Pila{
  string front;
  vector<string> p;
  void add(string last){
    front = last;
    p.push_back(last);
  }
  void popit(){
    p.pop_back();
    front = (p.size() > 0) ? p.back() : "@@";
  }
  void reset(){
    p.clear();
  }
};

void change(vector<Pila> &v, int &n, int d){
  v.at(n-d).add(v.at(n).front);
  v.at(n).popit();
  if (v.at(n).p.size() == 0){
    v.erase(v.begin()+n, v.begin()+n+1);
  }
  n-= (d == 3) ? 4 : 2;
}

void arrange(vector<Pila> &v){
  for (int n = 0; n < v.size(); n++){
    if (n-3 >= 0 && (v.at(n).front.at(0) == v.at(n-3).front.at(0) || v.at(n).front.at(1) == v.at(n-3).front.at(1))){
      change(v, n, 3);
    } else if (n-1 >= 0 && (v.at(n).front.at(0) == v.at(n-1).front.at(0) || v.at(n).front.at(1) == v.at(n-1).front.at(1))){
      change(v, n, 1);
    }
  }
}

int main(){
  int tmp;
  string card;
  vector<Pila> v;
  Pila pila;
  cin >> card;
  while(card != "#"){
    pila.add(card);
    v.push_back(pila);
    pila.reset();
    tmp = 51;
    while(tmp--){
      cin >> card;
      pila.add(card);
      v.push_back(pila);
      pila.reset();
    }
    arrange(v);
    string message = (v.size() != 1) ? " piles remaining: " : " pile remaining: ";
    cout << v.size() << message;
    for(int n = 0; n < v.size(); n++){
      if (n != v.size()-1) cout << v.at(n).p.size() << " ";
      else cout << v.at(n).p.size() << endl;
    }
    v.clear();
    cin >> card;
  }
  return 0;
}
