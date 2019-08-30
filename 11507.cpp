#include <iostream>
#include <string>
using namespace std;

class Angulo{
private:
  string angulo;
public:
  Angulo(){
    angulo = "+x";
  }

  void decide(string &desicion){
    if (desicion != "No")
      if (desicion == "+x") {angulo = desicion;}
      else if (desicion == "-x"){
        if (angulo == "+x") angulo = "-x";
        else if (angulo == "-x") angulo = "+x";
        else if (angulo == "+y") angulo = "-y";
        else if (angulo == "-y") angulo = "+y";
        else if (angulo == "+z") angulo = "-z";
        else if (angulo == "-z") angulo = "+z";
      }
      else if (desicion == "+y"){
        if (angulo == "+x") angulo = "+y";
        else if (angulo == "-x") angulo = "-y";
        else if (angulo == "+y") angulo = "-x";
        else if (angulo == "-y") angulo = "+x";
      }
      else if (desicion == "-y"){
        if (angulo == "+x") angulo = "-y";
        else if (angulo == "-x") angulo = "+y";
        else if (angulo == "+y") angulo = "+x";
        else if (angulo == "-y") angulo = "-x";
      }
      else if (desicion == "+z"){
        if (angulo == "+x") angulo = "+z";
        else if (angulo == "-x") angulo = "-z";
        else if (angulo == "+z") angulo = "-x";
        else if (angulo == "-z") angulo = "+x";
      }
      else if (desicion == "-z"){
        if (angulo == "+x") angulo = "-z";
        else if (angulo == "-x") angulo = "+z";
        else if (angulo == "+z") angulo = "+x";
        else if (angulo == "-z") angulo = "-x";
      }
  }

  void responder(){
    cout << angulo << endl;
  }
  void reset(){
    angulo = "+x";
  }
};

int main(){
  Angulo a;
  int cs;
  string o;
  cin >> cs;
  while(cs > 0){
    cs--;
    while(cs--){
      cin >> o;
      a.decide(o);
    }
    a.responder();
    a.reset();
    cin >> cs;
  }
  return 0;
}
