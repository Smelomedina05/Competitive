#include <iostream>
using namespace std;

void conteo(int &acum, int &fh, int &fm, int &sh, int &sm){
  if (fm > sm){
    acum += 60-fm+sm;
    sh = (sh == 0) ? 23 : sh-1;
  } else {
    acum += sm-fm;
  }
  if (fh > sh) acum += (24-fh+sh)*60;
  else acum+= (sh-fh)*60;
}

int main(){
  int fh, fm, sh, sm;
  int acum = 0;
  cin >> fh >> fm >> sh >> sm;
  while (fh != 0 || fm != 0 || sh != 0 || sm != 0){
    conteo(acum, fh, fm, sh, sm);
    cout << acum << endl;
    acum = 0;
    cin >> fh >> fm >> sh >> sm;
  }
  return 0;
}
