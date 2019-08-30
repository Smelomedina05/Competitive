#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

struct Major{
  string nota;
  vector<string> escala;
};

void scales(vector<Major> &majors, string *notes, int ns, int ms){
  int count = 0, nota;
  int instructions[7] = {2,2,1,2,2,2,1};
  Major scala;
  for (int n = 0; n < ns; n++){
    nota = n;
    for (int m = 0; m < ms; m++){
      scala.escala.push_back(notes[nota]);
      nota+= instructions[count++];
    }
    scala.nota = scala.escala.at(0);
    majors.push_back(scala);
    count = 0;
    scala.escala.clear();
  }
}

void encontrar(vector<Major> &m, vector<string> &v, vector<string> &final){
  int esta = 0, noesta = 0;
  vector<Major>::iterator it;
  vector<string>::iterator ti;
  for (it = m.begin(); it != m.end(); it++){
    for (int n = 0; n < v.size(); n++){
      if (find(it->escala.begin(), it->escala.end(), v.at(n)) != it->escala.end()){
        esta++;
      } else {
        noesta++;
      }
    }
    if (esta >= 1 && noesta == 0) final.push_back(it->nota);
    esta = 0;
    noesta = 0;
  }
}

void ordenar(string &data, vector<string> &v){
  string temporal;
  istringstream datos(data);
  while (datos >> temporal)
    v.push_back(temporal);
}


int main(){
  vector<Major> m;
  vector<string> v, final;
  string data;
  string notes[24] = {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
                      "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"};
  scales(m, notes, 12, 8);
  getline(cin, data);
  while(data != "END"){
    ordenar(data, v);
    encontrar(m, v, final);
    for (int n = 0; n < final.size(); n++)
      if (n == 0) cout << final.at(n);
      else cout << " " << final.at(n);
    cout << endl;
    data = "";
    v.clear();
    final.clear();
    getline(cin, data);
  }

  return 0;
}
