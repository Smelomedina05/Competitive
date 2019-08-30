#include <iostream>
#include <deque>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct Pos {
  int fila;
  int columna;
  bool operator==(const Pos& a) const {
    return (fila == a.fila &&  columna == a.columna);
  }
};

class Robot{
private:
  deque<char> orientacion;
  int fila;
  int columna;
public:
  Robot(){
    orientacion.push_back('N');
    orientacion.push_back('E');
    orientacion.push_back('S');
    orientacion.push_back('W');
    fila = 0;
    columna = 0;
  }
  void decide(char instruction, vector<Pos> &v){
    if (instruction == 'R') right();
    else if (instruction == 'L') left();
    else if (instruction == 'F') forward(v);
  }
  char getOrientacion(){
    return orientacion.front();
  }
  void setFila(int fila){
    this->fila = fila;
  }
  void setColumna(int columna){
    this->columna = columna;
  }
  int getFila(){
    return fila;
  }
  int getColumna(){
    return columna;
  }
  void left(){
    orientacion.push_front(orientacion.back());
    orientacion.pop_back();
  }
  void right(){
    orientacion.push_back(orientacion.front());
    orientacion.pop_front();
  }
  void forward(vector<Pos> &v){
    Pos tmp;
    int temp1 = fila, temp2 = columna;
    if (getOrientacion() == 'N') fila--;
    else if (getOrientacion() == 'E') columna++;
    else if (getOrientacion() == 'S') fila++;
    else if (getOrientacion() == 'W') columna--;
    tmp.fila = fila;
    tmp.columna = columna;
    if (find(v.begin(), v.end(), tmp) != v.end()){
      fila = temp1;
      columna = temp2;
    }
  }
  void reset(){
    orientacion.clear();
    orientacion.push_back('N');
    orientacion.push_back('E');
    orientacion.push_back('S');
    orientacion.push_back('W');
  }
};

int main(){
  Robot r;
  int t, row, column, fila = 1, count = 0;
  vector<Pos> paredes;
  Pos tmp;
  string linea;
  char order;
  cin >> t;
  while(t--){
    if (count != 0) cout << endl;
    getline(cin, linea);
    cin >> row >> column;
    row++;
    while(row--){
      getline(cin, linea);
      for (int n = 0; n < linea.size(); n++)
        if (linea.at(n) == '*'){
          tmp.fila = fila-1;
          tmp.columna = n+1;
          paredes.push_back(tmp);
        }
      fila++;
    }
    cin >> fila >> column;
    r.setFila(fila);
    r.setColumna(column);
    cin >> order;
    while (order != 'Q'){
      r.decide(order, paredes);
      cin >> order;
    }
    cout << r.getFila() << " " << r.getColumna() << " " << r.getOrientacion() << endl;
    count++;
    fila = 1;
    paredes.clear();
    r.reset();
  }
  return 0;
}
