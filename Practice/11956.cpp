#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

class Data{
private:
  int array[100];
  int crrnt;

public:
  Data(){
    crrnt = 0;
    for (int n = 0; n < 100; n++)
      array[n] = 0;
  }

  void determine(char instruction){
    if (instruction == '+')
      more();
    else if (instruction == '-')
      less();
    else if (instruction == '>')
      increment();
    else if (instruction == '<')
      decrement();
  }

  void increment(){
    if (crrnt == 99) crrnt = 0;
    else crrnt++;
  }
  void decrement(){
    if (crrnt == 0) crrnt = 99;
    else crrnt--;
  }
  void less(){
    if (array[crrnt] == 0) array[crrnt] = 255;
    else array[crrnt]--;
  }
  void more(){
    if (array[crrnt] == 255) array[crrnt] = 0;
    else array[crrnt]++;
  }

  void reset(){
    crrnt = 0;
    for (int n = 0; n < 100; n++)
      array[n] = 0;
  }

  int* entregar(){
    return array;
  }
};

int main(){
  int t, c = 1;
  Data d;
  string instruction;
  cin >> t;
  while (t--){
    cin >> instruction;
    for (int n = 0; n < instruction.size(); n++)
      d.determine(instruction.at(n));
    cout << "Case " << c << ": ";
    for (int n = 0; n < 100; n++)
      if (n == 99) printf("%02X", d.entregar()[n]);
      else printf("%02X ", d.entregar()[n]);
    cout << endl;
    d.reset();
    c++;
  }
  return 0;
}
