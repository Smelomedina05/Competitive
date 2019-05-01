#include <iostream>
#include <vector>
#include <deque>
#include <stdio.h>
using namespace std;

struct Space{
  char num;
  int inouts = 0;
  int in = 0;
  void add(){
    if (in == 1){
      inouts++;
      in = 0;
    } else {
      in++;
    }
  }
  void reset(){
    inouts = 0;
    in = 0;
  }
};

struct Location{
  int row = 0;
  int column = 0;
  void set(int n, int m){
    row = n;
    column = m;
  }
};

class Raton{
private:
  deque<char> orientacion;
  vector<vector<Space>> maze;
  Location l, start;
  int limx, limy;

public:
  Raton(){}

  void setMaze(vector<vector<Space>> maze){
    this->maze = maze;
  }

  void setStart(Location start){
    this->start = start;
    this->l = start;
  }

  vector<vector<Space>> getMaze(){
    return maze;
  }

  Location getL(){
    return l;
  }

  void turnLeft(){
    this->orientacion.push_back(this->orientacion.front());
    this->orientacion.pop_front();
  }
  void turnRight(){
    this->orientacion.push_front(this->orientacion.back());
    this->orientacion.pop_back();
  }
  void avanzar(){
    if (this->orientacion.front() == 'N'){
      if (this->maze.at(l.row-1).at(l.column).num == '0') {
        this->maze.at(l.row).at(l.column).add();
        this->maze.at(l.row-1).at(l.column).add();
        l.row--;
      }
      else turnLeft();
    } else if (this->orientacion.front() == 'W'){
      if (this->maze.at(l.row).at(l.column-1).num == '0') {
        this->maze.at(l.row).at(l.column).add();
        this->maze.at(l.row).at(l.column-1).add();
        l.column--;
      }
      else turnLeft();
    } else if (this->orientacion.front() == 'S'){
      if (this->maze.at(l.row+1).at(l.column).num == '0') {
        this->maze.at(l.row).at(l.column).add();
        this->maze.at(l.row+1).at(l.column).add();
        l.row++;
      }
      else turnLeft();
    } else if (this->orientacion.front() == 'E'){
      if (this->maze.at(l.row).at(l.column+1).num == '0') {
        this->maze.at(l.row).at(l.column).add();
        this->maze.at(l.row).at(l.column+1).add();
        l.column++;
      }
      else turnLeft();
    }
  }
  bool isRight(){
    if (this->orientacion.front() == 'N'){
      return (this->maze.at(l.row).at(l.column+1).num == '1') ? true : false;
    } else if (this->orientacion.front() == 'W'){
      return (this->maze.at(l.row-1).at(l.column).num == '1') ? true : false;
    } else if (this->orientacion.front() == 'S'){
      return (this->maze.at(l.row).at(l.column-1).num == '1') ? true : false;
    } else if (this->orientacion.front() == 'E'){
      return (this->maze.at(l.row+1).at(l.column).num == '1') ? true : false;
    }
    return false;
  }
  bool condicion(){
    return (l.row == start.row && l.column == start.column && orientacion.front() != 'E');
  }
  void decidir(){
    if (!isRight()){
      turnRight();
      avanzar();
    } else {
      avanzar();
    }
  }
  void conteo(int *veces){
    for (int rw = 1; rw <= limy; rw++)
      for (int co = 1; co <= limx; co++)
        switch (this->maze.at(rw).at(co).inouts){
          case 0:
            veces[0]++;
            break;
          case 1:
            veces[1]++;
            break;
          case 2:
            veces[2]++;
            break;
          case 3:
            veces[3]++;
            break;
          case 4:
            veces[4]++;
            break;
          default:
            break;
        }
  }
  void setAll(int n, int m, int *veces){
    char o[] = {'E','N', 'W', 'S'};
    this->orientacion.assign(o, o+4);
    this->limy = n;
    this->limx = m;
    this->maze.clear();
    for (int f = 0; f < 5; f++) veces[f] = 0;
  }

};

int main(){
  int n, m;
  Raton r;
  Space tmp;
  Location ltmp;
  vector<vector<Space>> maze;
  vector<Space> tmpmaze;
  int v[5];
  cin >> n >> m;
  while (n!=0 && m!=0){
    r.setAll(n, m, v);
    ltmp.set(0,0);
    for (int rw = 0; rw <= n+1; rw++){
      for (int co = 0; co <= m+1; co++){
        if (rw != 0 && co != 0 && rw != n+1 && co != m+1) cin >> tmp.num, tmp.inouts = (tmp.num == '1') ? 5 : 0;
        else tmp.num = '1';
        tmpmaze.push_back(tmp);
        ltmp.set((tmp.num != '1') ? rw : ltmp.row, 0);
      }
      maze.push_back(tmpmaze);
      tmpmaze.clear();
    }

    for (int rw = n+1; rw >= 0; rw--){
      for (int co = 0; co <= m+1; co++){
        ltmp.set(ltmp.row, (maze.at(rw).at(co).num != '1' && ltmp.column == 0) ? co : ltmp.column);
      }
    }

    r.setMaze(maze);
    r.setStart(ltmp);
    maze.clear();

    /*cout << ltmp.row << ltmp.column << endl;
    for (int rw = 0; rw < n+2; rw++){
      for (int co = 0; co < m+2; co++){
        cout << r.getMaze().at(rw).at(co).num << " ";
      }
      cout << endl;
    }*/

    while(!r.condicion()){
      r.decidir();
    }
    r.conteo(v);
    for (int f = 0; f < 5; f++) printf((to_string(v[f]).size() == 2) ? " %d" : ((to_string(v[f]).size() < 2) ? "  %d" : "%d"),v[f]);
    cout << endl;
    cin >> n >> m;
  }
  return 0;
}
