#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

void full(map<char, string> &m, char *characters, int csize){
  int counter = 2;
  for (int n = 0; n < csize; n++){
    if (n%3 == 0 && n != 0) counter++;
    m.insert({characters[n], to_string(counter)});
  }
}


int main(){
  int t, cs, counter = 0, cc = 0;
  map<char, string> m;
  map<string, int> c;
  map<string, int>::iterator cit;
  string numero, decode = "";
  string num = "1234567890";
  string::iterator it;
  char characters[24] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                      'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'};
  full(m, characters, 24);

  cin >> t;
  while (t--){
    getline(cin, numero);
    if (cc != 0) cout << endl;
    cin >> cs;
    while (cs--){
      cin >> numero;
      for (int n = 0; n < numero.size(); n++)
        if (numero.at(n) != '-'){
          if (num.find(numero.at(n)) != string::npos) decode += numero.at(n);
          else decode += m[numero.at(n)];
        }
      if (c.find(decode) != c.end()) c[decode] = c[decode] + 1;
      else c.insert({decode, 1});
      decode = "";
    }
    for (cit = c.begin(); cit != c.end(); cit++)
      if (cit->second >= 2){
        cout << cit->first.substr(0,3) << "-" << cit->first.substr(3,4)<< " " << cit->second << endl;
        counter++;
      }

    if (counter == 0) cout << "No duplicates." << endl;
    counter = 0;
    c.clear();
    cc++;
  }

  return 0;
}
