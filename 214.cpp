#include <iostream>
#include <string>
using namespace std;

void add(char &anterior, int &counter){
  if (anterior != '{'){
    cout << "A " << anterior << endl;
    anterior = '{';
  } else {
    cout << "A $" << --counter << endl;
  }
}

void sub(char &anterior, int &counter){
  if (anterior != '{'){
    cout << "S " << anterior << endl;
    anterior = '{';
  } else {
    cout << "N" << endl << "A $" << --counter << endl;
  }
}

void mul(char &anterior, int &counter){
  if (anterior != '{'){
    cout << "M " << anterior << endl;
    anterior = '{';
  } else {
    cout << "M $" << --counter << endl;
  }
}

void div(char &anterior, int &counter){
  if (anterior != '{'){
    cout << "D " << anterior << endl;
    anterior = '{';
  } else {
    cout << "ST $" << counter-- << endl << "L $" << counter++ << endl << "D $" << counter-- << endl;
  }
}

void neg(char &anterior, int &counter, bool &validado){
  if (anterior != '{'){
    if (validado) cout << "ST $" << counter++ << endl;
    cout << "L " << anterior << endl;
    anterior = '{';
    validado = true;
  }
  cout << "N" << endl;
}

void letter(char c, char &anterior, int &counter, bool &validado){
  if (anterior != '{'){
    if (validado) cout << "ST $" << counter++ << endl;
    cout << "L " << anterior << endl;
    validado = true;
  }
  anterior = c;
}

int main(){
  string s;
  bool validado = false;
  char anterior = '{';
  int counter = 0, t = 0;
  while (cin >> s){
    if (t++ != 0) cout << endl;
    s += '{';
    for (int n = 0; n < s.size(); n++){
      switch (s.at(n)) {
        case '+':
          add(anterior, counter);
          break;
        case '-':
          sub(anterior, counter);
          break;
        case '*':
          mul(anterior, counter);
          break;
        case '/':
          div(anterior, counter);
          break;
        case '@':
          neg(anterior, counter, validado);
          break;
        default:
          letter(s.at(n), anterior, counter, validado);
          break;
      }
    }
    validado = false;
    counter = 0;
  }

  return 0;
}
