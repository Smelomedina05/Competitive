#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Person{
  string nombre;
  int diferencia;
};

void edit(vector<Person> &ps, string nombre, int t, int c){
  for (int n = 0; n<ps.size(); n++){
    if (ps.at(n).nombre == nombre){
      ps.at(n).diferencia += (c > 0) ? t/c : 0;
    }
  }
}

void add(vector<Person> &ps, string nombre, int t, int c){
  for (int n = 0; n<ps.size(); n++){
    if (ps.at(n).nombre == nombre){
      ps.at(n).diferencia -= (c > 0) ? t - t%c : 0;
    }
  }
}

int main(){
  int cs, cut, temporal, tt, count = 0;
  vector<Person> personas;
  string nombre;
  while (cin >> cs){
    if (count != 0)
      cout << endl;
    temporal = cs;
    while (temporal--){
      Person p;
      cin >> p.nombre;
      p.diferencia = 0;
      personas.push_back(p);
    }
    while (cs--){
      cin >> nombre;
      cin >> temporal >> cut;
      add(personas, nombre, temporal, cut);
      tt = cut;
      while(tt--){
        cin >> nombre;
        edit(personas, nombre, temporal, cut);
      }
    }

    for (int n = 0; n < personas.size(); n++){
      cout << personas.at(n).nombre << " " << personas.at(n).diferencia << endl;
    }
    personas.clear();
    count++;
  }
  return 0;
}
