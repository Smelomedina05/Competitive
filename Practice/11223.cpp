#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

void llenarMapa(map<string, char> &code, string *codes, char *letters, int s){
  for (int n = 0; n < s; n++){
    code.insert({codes[n], letters[n]});
  }
}


void tranform(string &take, vector<string> &words){
  string guardado = "";
  for (int n = 0; n < take.size(); n++){
    if (take.at(n) == ' ') {
      if (guardado != ""){
        words.push_back(guardado);
        if (n+1 < take.size()) if (take.at(n+1) == ' ') words.push_back("@@@");
        guardado = "";
      }
    } else {
      guardado += take.at(n);
    }
  }
  if (guardado != "") words.push_back(guardado);
}

int main(){
  map<string, char> code;
  string codes[54] = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                  "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                  "...-", ".--", "-..-", "-.--", "--..", "-----",
                  ".----", "..---", "...--", "....-", ".....", "-....",
                  "--...", "---..", "----.", ".-.-.-", "--..--", "..--..",
                  ".----.", "-.-.--", "-..-.", "-.--.", "-.--.-", ".-...",
                  "---...", "-.-.-.", "-...-", ".-.-.", "-....-",
                  "..--.-", ".-..-.", ".--.-.", "@@@"};
  char comilla = "' "[0];
  char letras[55] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6',
                    '7', '8', '9', '.', ',', '?', comilla, '!', '/', '(', ')',
                    '&', ':', ';', '=', '+', '-', '_', '"', '@', ' '};

  llenarMapa(code, codes, letras, 55);

  int t, c = 1;
  cin >> t;
  cin.ignore();
  string message, decoded;
  vector<string> words;
  while (t--){
    if (c != 1) cout << endl;
    getline(cin, message);
    tranform(message, words);
    cout << "Message #" << c << endl;
    for (int n = 0; n < words.size(); n++){
      cout << code[words.at(n)];
    }
    cout << endl;
    decoded = "";
    words.clear();
    c++;
  }
  return 0;
}
